import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
from streamlit_drawable_canvas import st_canvas

# Load model
model = tf.keras.models.load_model(
    "models/digit_cnn_model.keras"
)

st.set_page_config(
    page_title="Handwritten Digit Recognition",
    page_icon="✍️"
)

st.title("✍️ Handwritten Digit Recognition")
st.write("Draw a digit (0-9) and click Predict.")

# Canvas
canvas_result = st_canvas(
    fill_color="black",
    stroke_width=15,
    stroke_color="white",
    background_color="black",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas",
)

if st.button("Predict"):

    if canvas_result.image_data is not None:

        # Convert canvas to grayscale
        img = canvas_result.image_data[:, :, 0]

        # Resize to MNIST size
        image = Image.fromarray(
            img.astype(np.uint8)
        ).resize((28, 28))

        img_array = np.array(image)

        # Normalize
        img_array = img_array.astype("float32") / 255.0

        # Show processed image
        st.image(
            img_array,
            caption="Processed 28x28 Image",
            width=150
        )

        # Reshape
        img_array = img_array.reshape(
            1, 28, 28, 1
        )

        # Predict
        prediction = model.predict(
            img_array,
            verbose=0
        )

        digit = np.argmax(prediction)
        confidence = np.max(prediction) * 100

        st.success(
            f"Predicted Digit: {digit}"
        )

        st.info(
            f"Confidence: {confidence:.2f}%"
        )

        st.write("Prediction Probabilities")

        for i in range(10):
            st.write(
                f"{i}: {prediction[0][i]*100:.2f}%"
            )