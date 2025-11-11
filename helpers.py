from flask import jsonify

def rest_response(message: str):
    return jsonify({
        "status": "OK",
        "result": message
    })

def rest_error(message: str):
    return jsonify({
        "status": "ERROR",
        "result": message
    }), 400
