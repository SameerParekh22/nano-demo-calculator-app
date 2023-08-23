from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return "Welcome to the Calculator API!"

@app.route("/calculator/add", methods=['POST'])
def add():
    try:
        data = request.json  # Assuming the request contains JSON data
        num1 = data.get('num1')
        num2 = data.get('num2')
        
        result = num1 + num2
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    try:
        data = request.json  # Assuming the request contains JSON data
        num1 = data.get('num1')
        num2 = data.get('num2')
        
        result = num1 - num2
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
