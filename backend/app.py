from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

CORS(
    app,
    resources={r"/*": {"origins": "*"}},
    supports_credentials=False
)

@app.route("/calculate", methods=["POST", "OPTIONS"])
def calculate():
    data = request.json

    a = float(data["num1"])
    b = float(data["num2"])
    op = data["operation"]

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        result = a / b if b != 0 else "Cannot divide by zero"
    else:
        result = "Invalid operation"

    return jsonify({"result": result})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
