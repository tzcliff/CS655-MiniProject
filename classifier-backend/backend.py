from flask import request, Flask, render_template
import time
import os
from werkzeug.utils import secure_filename
from classifier import ImageRecognition

app = Flask(__name__)
root = os.path.dirname(__file__)
img_folder = os.path.join(root, 'images')
if not os.path.exists(img_folder):
	os.makedirs(img_folder)

# root content
@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
	# Receive the file
	if request.method == 'POST':
		start_time = time.time()
		file = request.files['image']
		file.save(os.path.join(img_folder, secure_filename(file.filename)))


@app.route('/predict/<path:image_path>', methods=['GET', 'POST'])
def predict(image_path):
	if request.method == 'POST':
		recognizer = ImageRecognition(os.path.join(root, image_path))
		return recognizer.predict()


if __name__ == '__main__':
	app.run()