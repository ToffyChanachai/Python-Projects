from flask import Flask#, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

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
        "code": "007"
    }