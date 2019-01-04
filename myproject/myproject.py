
from flask import Flask, request, jsonify
from flask import render_template
from flask_cors import CORS
import json
from pathlib import Path
from datetime import datetime
from hashlib import sha256
application = Flask(__name__)
CORS(application)

@application.route("/")
def hello():
  return render_template('index.html', title='Home', user='Someone')

if __name__ == "__main__":
    application.run(host='0.0.0.0')
