from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)


words = [
    {
        "inputs": 3,
        "category": "Kpop",
        "word": "BTS"
    },
    {
        "inputs": 4,
        "category": "largest continent",
        "word": "Asia"
    },
    {
        "inputs": 7,
        "category": "Liquid metal",
        "word": "Mercury"
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-template")
def get_template():
    return jsonify({
        "status": "success",
        "word": random.choice(words)
    })
    

if __name__ == "__main__":
    app.run(debug=True)