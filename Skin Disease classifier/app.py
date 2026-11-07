from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
import cv2
import os

app = Flask(__name__)

model = tf.keras.models.load_model('skin_disease_model.h5')

classes = ['acne', 'eczema', 'melanoma', 'psoriasis']

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def predict_image(path):
    image = cv2.imread(path)
    image = cv2.resize(image, (128, 128))
    image = image / 255.0
    image = np.reshape(image, [1, 128, 128, 3])

    prediction = model.predict(image)
    predicted_class = classes[np.argmax(prediction)]

    return predicted_class

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None

    if request.method == 'POST':
        file = request.files['file']

        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            prediction = predict_image(filepath)

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)