import tensorflow as tf
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Load trained model
model = tf.keras.models.load_model("flower_model.keras")

# Class names
class_names = ["daisy", "dandelion", "roses", "sunflowers", "tulips"]

# Image path
img_path = "flower.jpg"

# Load image
img = image.load_img(img_path, target_size=(150, 150))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = img_array / 255.0

# Prediction
prediction = model.predict(img_array)

predicted_class = class_names[np.argmax(prediction)]
confidence = np.max(prediction) * 100

print("Predicted Flower:", predicted_class)
print(f"Confidence: {confidence:.2f}%")