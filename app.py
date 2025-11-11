from flask import Flask
from helpers import rest_response, rest_error

app = Flask(__name__)

def is_a_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

@app.route('/restcalc/<arg1>/plus/<arg2>', methods=['GET'])
def add(arg1, arg2):
    if not (is_a_number(arg1) and is_a_number(arg2)):
        return rest_error("Invalid arguments.")
    answer = float(arg1) + float(arg2)
    return rest_response(str(answer))

@app.route('/restcalc/<arg1>/minus/<arg2>', methods=['GET'])
def subtract(arg1, arg2):
    if not (is_a_number(arg1) and is_a_number(arg2)):
        return rest_error("Invalid arguments.")
    answer = float(arg1) - float(arg2)
    return rest_response(str(answer))

@app.route('/restcalc/<arg1>/times/<arg2>', methods=['GET'])
def multiply(arg1, arg2):
    if not (is_a_number(arg1) and is_a_number(arg2)):
        return rest_error("Invalid arguments.")
    answer = float(arg1) * float(arg2)
    return rest_response(str(answer))

@app.route('/restcalc/<arg1>/dividedby/<arg2>', methods=['GET'])
def divide(arg1, arg2):
    if not (is_a_number(arg1) and is_a_number(arg2)):
        return rest_error("Invalid arguments.")
    try:
        answer = float(arg1) / float(arg2)
    except ZeroDivisionError:
        return rest_error("Division by zero.")
    return rest_response(str(answer))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
