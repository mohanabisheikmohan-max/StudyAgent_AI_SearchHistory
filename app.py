import os

from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

from agent import run_agent

load_dotenv()

app = Flask(__name__)

app.config["MAX_CONTENT_LENGTH"] = 2 * 1024 * 1024


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json(silent=True) or {}

    question = (data.get("question") or "").strip()

    if not question:
        return jsonify({
            "ok": False,
            "error": "Please enter a question."
        }), 400

    try:

        answer = run_agent(question)

        return jsonify({
            "ok": True,
            "answer": answer
        })

    except Exception as e:

        print("ERROR:", e)

        return jsonify({
            "ok": False,
            "error": "AI service error. Please try again."
        }), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=True
    )