from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='font-size: 14px; color: blue;'>Hello, World!</h1>"

# @app.route("/json", methods=['GET'])
# def json():
#     if request.method == 'GET':
#     return jsonify([{
#         "code": "007"
#     }, {
#         "code": "001"
#     }])

@app.route("/json")
def json():
    return {
        "code": "007",
        "name": "test"
    }