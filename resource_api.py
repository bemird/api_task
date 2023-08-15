from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/resource", methods=["GET"])
def get_resource():
    # Simulate checking the validity of the token and providing access
    token = request.headers.get("Authorization", "").split(" ")[1]
    
    if validate_token(token):
        return json.dumps({"message": "Access granted to the resource"})
    else:
        return json.dumps({"message": "Access denied"}), 401

def validate_token(token):
    # Simulate token validation logic
    return token.startswith("token-")

if __name__ == "__main__":
    app.run(port=9000)

