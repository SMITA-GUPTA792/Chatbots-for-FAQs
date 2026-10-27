# AI FAQ Chatbot

A FAQ chatbot about **Artificial Intelligence**. It preprocesses text with **NLTK**
(tokenize, remove stopwords, lemmatize), matches the user's question against a set
of FAQs using **TF-IDF + cosine similarity**, and returns the best-matching answer
through a simple web chat UI.

## How it works

1. **`faqs.py`** — the FAQ dataset (30 question/answer pairs about AI).
2. **`chatbot.py`** — the NLP engine:
   - `preprocess()` lowercases text, expands abbreviations (`ai` → `artificial
     intelligence`, `ml` → `machine learning`, ...), tokenizes, removes stopwords,
     and lemmatizes using NLTK (falls back to a lightweight built-in tokenizer if
     NLTK/its data isn't available, so the bot still runs offline).
   - `FAQChatbot` builds a TF-IDF index over all FAQ questions at startup. For
     each user message, it vectorizes the cleaned text and computes **cosine
     similarity** against every FAQ question, returning the answer for the
     highest-scoring match (or a fallback message if nothing scores above the
     similarity threshold).
3. **`app.py`** — a small Flask server with two routes:
   - `GET /` — serves the chat UI (`templates/index.html`)
   - `POST /get_response` — accepts `{"message": "..."}` and returns the matched
     answer + matched question + confidence score as JSON.
4. **`templates/` + `static/`** — the browser chat UI (HTML/CSS/JS) that calls
   `/get_response` and renders the conversation. Each bot reply shows which FAQ
   it matched and the similarity score, so you can see the matching at work.

   ## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `flask` | Web framework & routing |
| `nltk` | Tokenisation, stopword removal, lemmatisation |
| `scikit-learn` | TF-IDF vectorisation + cosine similarity |
| `numpy` | Numerical operations |

Install all at once:

```bash
pip install -r requirements.txt
```

Contents of `requirements.txt`:
flask

nltk

scikit-learn

numpy


## Setup

```bash
pip install -r requirements.txt
```

The first run will download a few small NLTK data packages (punkt, stopwords,
wordnet) if they aren't already present — this needs an internet connection once.

## Run the web chat UI

```bash
python app.py or streamlit app.py
```

Then open **http://127.0.0.1:5000** in your browser.

## Run it from the command line instead

```bash
python chatbot.py
```

This starts a quick terminal chat loop (type `quit` to exit) — useful for testing
the matching logic without spinning up Flask.

## 🛠️ Customisation

### Add or edit FAQ questions

Open `faqs.py`. Each entry follows this structure:

```python
{
    "question": "What is reinforcement learning?",
    "answer": "Reinforcement learning is a type of ML where an agent learns by interacting with an environment...",
    "category": "Machine Learning"
}
```

Add as many entries as you like — the TF-IDF model rebuilds automatically on every server start.

### Change the similarity threshold

In `app.py`:

```python
bot = FAQChatbot(FAQS, similarity_threshold=0.2)
```

- **Lower** (e.g. `0.1`) → matches more loosely, fewer "I don't know" replies
- **Higher** (e.g. `0.4`) → stricter matching, more fallback replies

### Swap the avatar image

Replace `static/robot.jpeg` with any square image and keep the same filename, or update the `src` in `index.html`.

---


## Project structure

```
faq_chatbot/

├── app.py                  # Flask server & routes

├── chatbot.py              # NLTK preprocessing + TF-IDF / cosine-similarity matching

├── faqs.py                 # FAQ dataset (Artificial Intelligence topics)

├── requirements.txt        # Python dependencies

├── templates/

│   └── index.html          # Home page + Chat UI markup (Jinja2)

└── static/

├── style.css           # Full UI styling (dark theme, animations)

├── script.js           # Chat UI logic — calls /get_response API

├── robot.jpeg          # AI assistant avatar image

└── Screenshot-chat.png # Chat page screenshot (for README)


## ✨ Features

- 🏠 **Home / Landing Page** — Animated welcome screen with feature highlights before entering the chat
- 🔍 **TF-IDF Matching** — Finds the closest FAQ answer using term frequency–inverse document frequency + cosine similarity
- 📊 **Confidence Scoring** — Every bot reply shows the match percentage and the matched FAQ question
- 🗂️ **Topic Sidebar** — All FAQ questions grouped by category; click any to ask instantly
- 🕓 **Question History** — Every question you ask is saved in the sidebar for quick re-use
- 💡 **Suggestion Chips** — Three quick-start questions shown below the chat window
- 📱 **Responsive Design** — Sidebar becomes a slide-in drawer on mobile screens
- ⚡ **Zero Page Reloads** — Fully async fetch-based chat; no form submissions

---

---

## 🎨 UI Overview

| File | Responsibility |
|------|---------------|
| `index.html` | Two-section layout: `#home-page` (landing) + `#chat-page` (chat); Jinja2 template |
| `style.css` | Dark theme (`#0b0f19` base), teal accent (`#5eead4`), Space Grotesk + Inter + JetBrains Mono fonts |
| `script.js` | Sidebar open/close, topic rendering from JSON, history tracking, async message send/receive |

### Home → Chat transition

Clicking **"Start Asking →"** on the home page triggers a smooth CSS fade-out + slide-up animation (0.6 s) before revealing the full chat interface — no page reload.

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 🙌 Credits

- Fonts: [Google Fonts](https://fonts.google.com/) — Space Grotesk, Inter, JetBrains Mono
- NLP: [NLTK](https://www.nltk.org/) + [scikit-learn](https://scikit-learn.org/)
- Framework: [Flask](https://flask.palletsprojects.com/)
