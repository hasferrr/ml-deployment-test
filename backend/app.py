import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import io
import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image

from flask import Flask, request, jsonify, make_response
from flask_cors import CORS


# ======================= Model Handler =======================

model = keras.models.load_model("nn.h5")

def transform_image(pillow_image):
  data = np.asarray(pillow_image)
  data = data / 255.0
  data = data[np.newaxis, ..., np.newaxis]
  # --> [1, x, y, 1]
  data = tf.image.resize(data, [28, 28])
  return data

def predict(x):
  predictions = model(x)
  predictions = tf.nn.softmax(predictions)
  pred0 = predictions[0]
  label0 = np.argmax(pred0)
  return label0

def predict_image_bytes_to_model(image_bytes):
  try:
    pillow_img = Image.open(io.BytesIO(image_bytes)).convert('L')
    tensor = transform_image(pillow_img)
    prediction = predict(tensor)
    return {"prediction": int(prediction)}
  except Exception as e:
    return {"error": str(e)}




# ======================= API Route Handler =======================

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET", "POST"])
def index():
  if request.method == "POST":
    file = request.files.get('file')

    if file is None or file.filename == "":
      return jsonify({"error": "no file"})

    image_bytes = file.read()
    result = predict_image_bytes_to_model(image_bytes)
    return jsonify(result)

  return "OK"


if __name__ == "__main__":
  app.run(debug=True)
