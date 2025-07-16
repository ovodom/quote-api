from flask import Flask, jsonify
import random

app = Flask(__name__)

quotes = [
    "Stay hungry, stay foolish.",
    "Simplicity is the ultimate sophistication.",
    "Code is like humor. When you have to explain it, it’s bad.",
]

@app.route('/quote', methods=['GET'])
def get_quote():
    return jsonify({'quote': random.choice(quotes)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
