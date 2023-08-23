from flask import Flask, request, jsonify

app = Flask(_name_)

@app.route('/calculator/greeting', methods=['GET'])
def greeting():
  return jsonify({'message': 'Welcome to the calculator service!'})

@app.route('/calculator/add', methods=['POST'])
def add():
  num1 = request.form.get('num1')
  num2 = request.form.get('num2')
  result = num1 + num2
  return jsonify({'result': result})

@app.route('/calculator/subtract', methods=['POST'])
def subtract():
  num1 = request.form.get('num1')
  num2 = request.form.get('num2')
  result = num1 - num2
  return jsonify({'result': result})


if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
