import flask
from flask.json import jsonify
# from werkzeug.wrappers import request
import logging

app = flask.Flask(__name__)
app.config["DEBUG"] = True


model = {
  'id': 14992,
  'date': '2021_04_05',
  'hyperparam.A': 53.2e-6
}

content = {}

@app.route('/api/v1/ml/model/hyperparams', methods=[ 'POST'])
def hyperparams():
    if flask.request.method == 'POST':
        request_data = flask.request.get_json()
        logging.info(request_data)
        return jsonify(request_data)




@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/api/v1/ml/model', methods=['GET'])
def api_id():
  return jsonify(model)

app.run()
