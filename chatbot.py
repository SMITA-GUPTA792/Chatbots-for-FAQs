"""
chatbot.py
----------
The "brain" of the FAQ chatbot.

Pipeline:
  1. Preprocess text with NLTK (lowercase, tokenize, remove stopwords, lemmatize).
  2. Convert all FAQ questions + the user's question into TF-IDF vectors.
  3. Use cosine similarity to find the FAQ question closest in meaning to
     what the user typed.
  4. Return the matching answer (or a fallback message if nothing scores
     high enough).

This file can also be run directly for a quick command-line chat:
    python chatbot.py
"""

import re
import string

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from faqs import FAQS

# ---------------------------------------------------------------------------
# NLTK setup
# ---------------------------------------------------------------------------
# We try to use NLTK for proper tokenization, stopword removal, and
# lemmatization. If NLTK (or its data files) aren't available — e.g. no
# internet access on first run — we fall back to a lightweight built-in
# preprocessor so the chatbot still works.

_NLTK_READY = False

try:
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    from nltk.stem import WordNetLemmatizer

    _REQUIRED_NLTK_DATA = [
        ("tokenizers/punkt", "punkt"),
        ("tokenizers/punkt_tab", "punkt_tab"),
        ("corpora/stopwords", "stopwords"),
        ("corpora/wordnet", "wordnet"),
        ("corpora/omw-1.4", "omw-1.4"),
    ]

    def _ensure_nltk_data():
        for path, name in _REQUIRED_NLTK_DATA:
            try:
                nltk.data.find(path)
            except LookupError:
                nltk.download(name, quiet=True)

    _ensure_nltk_data()
    _LEMMATIZER = WordNetLemmatizer()
    _STOPWORDS = set(stopwords.words("english"))
    _NLTK_READY = True
    print("[chatbot] Using NLTK for preprocessing (tokenize, stopwords, lemmatize).")

except Exception as exc:  # ImportError or download failure (e.g. no internet)
    print(f"[chatbot] NLTK unavailable ({exc}). Falling back to a built-in preprocessor.")
    _NLTK_READY = False

# Small fallback stopword list, only used if NLTK truly can't be loaded.
_FALLBACK_STOPWORDS = {
    "a", "an", "the", "is", "are", "was", "were", "be", "been", "being",
    "and", "or", "but", "if", "of", "at", "by", "for", "with", "about",
    "to", "from", "in", "on", "as", "it", "this", "that", "these", "those",
    "i", "you", "he", "she", "we", "they", "do", "does", "did", "can",
    "could", "should", "would", "what", "which", "who", "whom", "will",
    "my", "your", "his", "her", "its", "our", "their", "me", "him",
}


def _fallback_stem(word: str) -> str:
    """Very small suffix-stripping 'stemmer' used only when NLTK is unavailable."""
    for suffix in ("ing", "edly", "edness", "ed", "es", "s"):
        if word.endswith(suffix) and len(word) - len(suffix) > 2:
            return word[: -len(suffix)]
    return word


# Common AI abbreviations get expanded to their full form so that "AI" and
# "Artificial Intelligence" (or "ML" / "machine learning", etc.) are treated
# as the same concept by the vectorizer.
_ABBREVIATIONS = {
    "ai": "artificial intelligence",
    "ml": "machine learning",
    "dl": "deep learning",
    "nlp": "natural language processing",
    "agi": "artificial general intelligence",
    "llm": "large language model",
    "llms": "large language model",
}


def _expand_abbreviations(text: str) -> str:
    return " ".join(_ABBREVIATIONS.get(word, word) for word in text.split())


def preprocess(text: str) -> str:
    """
    Clean and normalize text:
      - lowercase
      - strip punctuation / non-alphanumeric characters
      - expand common abbreviations (ai -> artificial intelligence, etc.)
      - tokenize
      - remove stopwords
      - lemmatize (or lightly stem, in fallback mode)
    Returns a single space-joined string ready for TF-IDF vectorization.
    """
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = _expand_abbreviations(text)

    if _NLTK_READY:
        tokens = word_tokenize(text)
        cleaned = [
            _LEMMATIZER.lemmatize(tok)
            for tok in tokens
            if tok not in _STOPWORDS and tok not in string.punctuation and tok.strip()
        ]
    else:
        tokens = text.split()
        cleaned = [
            _fallback_stem(tok)
            for tok in tokens
            if tok not in _FALLBACK_STOPWORDS and tok.strip()
        ]

    return " ".join(cleaned)


# ---------------------------------------------------------------------------
# Matching engine
# ---------------------------------------------------------------------------
class FAQChatbot:
    """Matches a user's question to the closest FAQ using TF-IDF + cosine similarity."""

    def __init__(self, faqs=None, similarity_threshold: float = 0.2):
        self.faqs = faqs if faqs is not None else FAQS
        self.threshold = similarity_threshold

        self.questions = [item["question"] for item in self.faqs]
        self.processed_questions = [preprocess(q) for q in self.questions]

        # TF-IDF vectorizer fit once on all known FAQ questions.
        self.vectorizer = TfidfVectorizer()
        self.question_vectors = self.vectorizer.fit_transform(self.processed_questions)

    def get_response(self, user_input: str) -> dict:
        """
        Returns a dict:
          {
            "answer": str,
            "matched_question": str | None,
            "confidence": float   # cosine similarity score, 0-1
          }
        """
        cleaned = preprocess(user_input)

        if not cleaned.strip():
            return {
                "answer": "Could you rephrase that? I didn't catch a real question there.",
                "matched_question": None,
                "confidence": 0.0,
            }

        user_vector = self.vectorizer.transform([cleaned])
        similarities = cosine_similarity(user_vector, self.question_vectors).flatten()

        best_idx = int(similarities.argmax())
        best_score = float(similarities[best_idx])

        if best_score < self.threshold:
            return {
                "answer": (
                    "I'm not confident I have a good answer for that yet. "
                    "Try rephrasing, or ask something else about AI."
                ),
                "matched_question": None,
                "confidence": round(best_score, 3),
            }

        return {
            "answer": self.faqs[best_idx]["answer"],
            "matched_question": self.faqs[best_idx]["question"],
            "confidence": round(best_score, 3),
        }


# ---------------------------------------------------------------------------
# Command-line demo
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    bot = FAQChatbot()
    print("\nAI FAQ Chatbot (type 'quit' to exit)\n" + "-" * 40)
    while True:
        user_text = input("You: ").strip()
        if user_text.lower() in {"quit", "exit", "bye"}:
            print("Bot: Goodbye!")
            break
        result = bot.get_response(user_text)
        print(f"Bot: {result['answer']}")
        if result["matched_question"]:
            print(f"      (matched: \"{result['matched_question']}\", "
                  f"confidence: {result['confidence']})")
