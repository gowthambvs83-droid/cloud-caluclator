# Import Flask class (used to create server)
from flask import Flask, request, jsonify

# Import CORS to allow frontend to talk to backend
from flask_cors import CORS

# Create Flask app object
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Create API endpoint: /calculate
@app.route("/calculate", methods=["POST"])
def calculate():
    # Read JSON data sent from JavaScript
    data = request.json

    # Extract values from JSON
    a = float(data["num1"])
    b = float(data["num2"])
    op = data["operation"]

    # Perform calculation
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

    # Send result back as JSON
    return jsonify({"result": result})


# Run server
if __name__ == "__main__":
    app.run()

