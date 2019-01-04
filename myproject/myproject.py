
from flask import Flask, request, jsonify
from flask import render_template, redirect
from flask_cors import CORS
import json
from pathlib import Path
from datetime import datetime
from hashlib import sha256
from pathlib import Path
import os
from dataprepare import dataprepare
application = Flask(__name__)
CORS(application)

@application.route("/", methods=['GET', 'POST'])
def home():

	table_html = None
	if request.method == 'POST':
		Path('uploads').mkdir(exist_ok=True)
		print(request)
		print(request.files)
		if 'send_file' not in request.files:
			print('No file part')
			return redirect('/')

		file = request.files['send_file']
		if file.filename == '':
			print('No selected file')
			return redirect('/')
		if file:
			file.save(os.path.join('uploads/', file.filename))
	
		table_html = dataprepare(os.path.join('uploads/', file.filename))
	
	table_html = '' if not table_html else table_html
	return render_template('index.html', title='Home', user='Someone', table_html=table_html)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
