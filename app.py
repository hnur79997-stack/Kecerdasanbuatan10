from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)   # ← penting!

RESPONSES = [
    "Baik, saya mengerti.",
    "Bisa dijelaskan lebih lengkap?",
    "Oke, saya catat.",
    "Menarik sekali!",
    "Ada pertanyaan lainnya?"
]

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if "halo" in user_message.lower():
        bot_reply = "Halo juga! Ada yang bisa saya bantu?"
    elif "nama" in user_message.lower():
        bot_reply = "Nama saya Chatbot Flask."
    else:
        bot_reply = random.choice(RESPONSES)

    return jsonify({"reply": bot_reply})

@app.route("/")
def home():
    return "Server Chatbot Flask Aktif!"

if __name__ == "__main__":
    app.run(debug=True)
