import json
from collections import OrderedDict
from flask import Flask, render_template, request, jsonify
from chatbot import FAQChatbot
from faqs import FAQS

app = Flask(__name__)
bot = FAQChatbot(FAQS, similarity_threshold=0.2)

def build_topics(faqs):
    topics = OrderedDict()
    for item in faqs:
        topics.setdefault(item.get("category", "General"), []).append(item["question"])
    return topics

TOPICS = build_topics(FAQS)

@app.route("/")
def home():
    return render_template("index.html", topics_json=json.dumps(TOPICS))

@app.route("/get_response", methods=["POST"])
def get_response():
    data = request.get_json(silent=True) or {}
    user_message = (data.get("message") or "").strip()
    if not user_message:
        return jsonify({"answer": "Please type a question.", "matched_question": None, "confidence": 0})
    result = bot.get_response(user_message)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=False, use_reloader=False, threaded=True)