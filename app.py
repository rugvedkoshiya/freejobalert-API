import json
from flask import Flask, Response
from flask_cors import CORS
from script import getData

app = Flask(__name__)
CORS(app)
app.secret_key = "SECRET_KEY"

URL = "https://www.freejobalert.com/police-defence-jobs/"

@app.route("/", methods=['GET'])
def getDataAPI():
    response = Response(json.dumps(getData(URL)), status=200, mimetype='application/json')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == "__main__":
    app.run(debug = True)
