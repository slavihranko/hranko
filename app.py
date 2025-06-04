from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    messages = data.get("messages", [])

    client = openai.OpenAI()

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )

    return jsonify({"reply": response.choices[0].message.content})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
