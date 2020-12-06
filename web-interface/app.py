from flask import Flask, render_template, request
import requests
import time
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        url = "http://192.122.236.117:5000/predict"
        files = {'image': open(secure_filename(f.filename), 'rb')}
        start_time = time.time()
        r = requests.post(url, files=files)
        print("Total time: {:.3f}s".format(time.time() - start_time))

        return r.text

# @app.route('/output', methods=['GET', 'POST'])
# def upload():
#     # Receive the file
#     if request.method == 'POST':
#         print(str(request.data))
#         return str(request.data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



	

		
