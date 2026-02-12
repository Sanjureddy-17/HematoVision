from flask import Flask, render_template, request, redirect
import os
import cv2
import base64
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Load model once
model = load_model("Blood Cell.keras")

class_labels = ['eosinophil', 'lymphocyte', 'monocyte', 'neutrophil']


def predict_image_class(image_path, model):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Invalid image file")

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img_rgb, (224, 224))
    img_preprocessed = preprocess_input(img_resized.reshape(1, 224, 224, 3))

    predictions = model.predict(img_preprocessed)

    class_idx = np.argmax(predictions, axis=1)[0]
    confidence = float(np.max(predictions)) * 100

    return class_labels[class_idx], confidence, img_rgb


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":

        os.makedirs("static", exist_ok=True)

        file = request.files.get("file")
        if not file or file.filename == "":
            return redirect(request.url)

        filename = secure_filename(file.filename)
        file_path = os.path.join("static", filename)
        file.save(file_path)

        label, confidence, img_rgb = predict_image_class(file_path, model)

        _, img_encoded = cv2.imencode(
            ".png", cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)
        )
        img_str = base64.b64encode(img_encoded).decode("utf-8")

        return render_template(
            "result.html",
            class_label=label,
            confidence=round(confidence, 2),
            img_data=img_str
        )

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
