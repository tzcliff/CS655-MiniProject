from flask import request, Flask, render_template
import requests
import time
import os
from werkzeug.utils import secure_filename
import asyncio
from classifier import ImageRecognition

app = Flask(__name__)
loop = asyncio.get_event_loop()
result1 = ""

@app.route('/predict', methods=['GET', 'POST'])
def notify():
	if request.method == 'POST':
		#loop.run_until_complete(upload())
		#print("after")
		#url = "http://192.122.236.116:5000/output"
		#r = requests.post(url, data=result1)
		
		f = request.files['image']
		print("fname:" + f.filename)
		f.save(secure_filename(f.filename))
		start_time = time.time()
		try:
			result1 = ImageRecognition(secure_filename(f.filename)).predict()
			result1 += "\nProcessing time: {:.3f}s".format(time.time() - start_time)
			return render_template('output.html', value=result1)
		except:
			return render_template('output.html', value='Invalid File Type!!')
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
