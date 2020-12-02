import tensorflow as tf 
import numpy as np

from tensorflow.keras.applications.resnet50 import preprocess_input, ResNet50
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

INPUT_SHAPE = (224, 224)
MODEL_PATH = "model/softmax.h5"

class ImageRecognition():
    def __init__(self, inputPath):
        # Disable the GPU
        tf.config.set_visible_devices([], 'GPU') 

        self.model = self._getModel()
        self.input = self._loadImage(inputPath)

    def _loadImage(self, path):
        img = load_img(path, 
                       target_size = INPUT_SHAPE)

        imgArray = img_to_array(img)
        imgArray = tf.expand_dims(imgArray, 0) # create a batch
        imgArray = preprocess_input(imgArray)

        return imgArray

    def _getModel(self):
        resnet50 = ResNet50()
        dense = load_model(MODEL_PATH, compile = False)

        model = Sequential([resnet50, dense])
        for layer in model.layers:
            layer.trainable = False

        return model

    def predict(self):
        """
        Predict the category (cat or dog) of the current image
        """
        prediction = self.model.predict(self.input)

        idx = np.argmax(prediction, axis = 1)
        category = ("Cat" if idx == 0 else "Dog")

        result = "Predicted category: {}".format(category)

        # Debug
        # score = prediction[0, idx].item()
        # result = "Predicted category: {}\nScore: {}".format(category, score)

        return result

# Debug
# print(ImageRecognition("../data/dog4.jpg").predict())