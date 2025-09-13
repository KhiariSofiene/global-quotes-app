from flask import Flask, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

quotes = [
    {"author": "Albert Einstein", "text": "Life is like riding a bicycle. To keep your balance you must keep moving."},
    {"author": "Steve Jobs", "text": "Stay hungry, stay foolish."},
    {"author": "Maya Angelou", "text": "You will face many defeats in life, but never let yourself be defeated."},
    {"author": "Oscar Wilde", "text": "Be yourself; everyone else is already taken."},
    {"author": "Nelson Mandela", "text": "The greatest glory in living lies not in never falling, but in rising every time we fall."},
    {"author": "Confucius", "text": "It does not matter how slowly you go as long as you do not stop."},
    {"author": "Sappho", "text": "One loyal friend is worth ten thousand relatives."},
    {"author": "Leonardo da Vinci", "text": "Simplicity is the ultimate sophistication."},
    {"author": "Rumi", "text": "What you seek is seeking you."},
    {"author": "Amelia Earhart", "text": "The most effective way to do it, is to do it."}
]

@app.route("/quote", methods=["GET"])
def get_quote():
    return jsonify(random.choice(quotes)), 200

@app.route("/", methods=["GET"])
def root():
    return jsonify({"message":"Global Quotes API", "routes":["/quote"]}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
