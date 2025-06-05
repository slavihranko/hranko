from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Зареждане на системния промпт от файл
system_prompt = "Ти си личен диетолог. Изчисли нужните калории според тегло, ръст, възраст, пол и цел. След това създай примерно дневно меню – закуска, обяд, вечеря – с калории за всяко хранене и общо. Ако има алергии или забранени храни, не ги включвай. Пиши кратко, ясно и подредено."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    messages = data.get("messages", [])

    # Вкарваме системния промпт като първо съобщение
    messages.insert(0, {"role": "system", "content": system_prompt})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=messages
        )
        reply = response["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
