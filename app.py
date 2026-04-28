import random
from flask import Flask, jsonify

app = Flask(__name__)

quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "Stay hungry, stay foolish. - Steve Jobs",
    "Imagination is more important than knowledge. - Albert Einstein",
]


def get_random_quote():
    return random.choice(quotes)


@app.route("/")
def home():
    return jsonify({"quote": get_random_quote()})


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)