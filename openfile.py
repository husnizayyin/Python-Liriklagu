import tensorflow as tf
import numpy as np

# Load the model
model = tf.keras.models.load_model('mnist_model.h5')

# Display the model's architecture
model.summary()

# Load the MNIST dataset again
(test_images, _), _ = tf.keras.datasets.mnist.load_data()
test_images = test_images.reshape((10000, 28, 28, 1)).astype('float32') / 255

# Make predictions
predictions = model.predict(test_images)

# Print the predicted class for the first test image
predicted_class = np.argmax(predictions[0])
print(f"Predicted class for the first test image: {predicted_class}")
