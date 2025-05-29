import streamlit as st             # Streamlit for web UI
import requests                   # To send HTTP requests to FastAPI backend
from PIL import Image             # To handle image processing

# Set up the Streamlit page
st.set_page_config(page_title="🌼 Flower Classifier", layout="centered")
st.title("🌼 Flower Classification")

# File uploader widget to upload flower images
uploaded_file = st.file_uploader("📤 Upload a flower image (jpg/png)", type=["jpg", "jpeg", "png"])

# If an image has been uploaded
if uploaded_file is not None:
    try:
        # Open and display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="🖼️ Uploaded Image", use_column_width=True)

        st.write("📡 Sending file to FastAPI...")

        # Prepare the image file for the API request
        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}

        # Send the image to the FastAPI endpoint for prediction
        response = requests.post("http://127.0.0.1:8080/predict", files=files, timeout=60)

        # Raise an error if the request was unsuccessful
        response.raise_for_status()

        # Convert the JSON response into a Python dictionary
        result = response.json()

        st.success("✅ Received response from FastAPI")

        # Show raw JSON response for debugging
        st.json(result)

        # Check for error in response and display accordingly
        if "error" in result:
            st.error(f"❌ Error: {result['error']}")
        else:
            # Display the prediction result (class and confidence)
            st.markdown(f"""
            ### 🌸 Prediction Result
            - **Class**: `{result['class']}`
            - **Confidence**: `{result['confidence']:.2%}`
            """)

    # Handle errors in API call
    except requests.exceptions.RequestException as e:
        st.error(f"❌ API call failed: {e}")

    # Handle any other errors
    except Exception as e:
        st.error(f"❌ Unexpected error: {e}")

# Load the training dataset to get class names (for display or verification)
# This code would typically be placed in the training or backend part, not UI
train_ds = tf.keras.utils.image_dataset_from_directory(
    '/content/drive/MyDrive/model/dataset/train',  # Path to training dataset
    image_size=(224, 224),                         # Resize images to 224x224
    batch_size=32                                  # Batch size for loading
)

# Print the class names (e.g., ['daisy', 'rose', 'sunflower'])
print(train_ds.class_names)

# Save the class names to a variable for later use
class_names = train_ds.class_names
