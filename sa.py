from flask import Flask, jsonify, request

app = Flask(__name__)


data ={
'said bg':'test'
}

@app.route('/said', methods=['GET'])
def api():
    if request.method == 'GET':
        return jsonify(data)

if __name__ == '__main__':
    app.run(port=8080)