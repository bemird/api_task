from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route("/token", methods=["GET"])
def get_token():
    # Simulate generating a token and returning it to the client
    token = generate_random_token()
    return jsonify({"token": token})

def generate_random_token():
    return f"token-{random.randint(1000, 9999)}"

if __name__ == "__main__":
    app.run(port=8000)

