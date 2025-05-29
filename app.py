from fastapi import FastAPI, File, UploadFile       # FastAPI for building the API
from tensorflow.keras.models import load_model      # For loading the trained Keras model
from PIL import Image, UnidentifiedImageError       # To process uploaded images
import numpy as np                                  # For numerical computations
import io                                           # To handle in-memory byte streams

# Initialize FastAPI app
app = FastAPI()

# Load the trained flower classification model
model = load_model("C:/Users/publi/AI_model/flowers_model.keras")

# List of flower classes used during training
class_names = ['daisy', 'rose', 'sunflower']

# Preprocessing function: resize image and normalize pixel values
def preprocess(img):
    img = img.resize((224, 224))              # Resize image to 224x224 (as expected by the model)
    img_array = np.array(img) / 255.0         # Normalize pixel values to [0, 1]
    return np.expand_dims(img_array, axis=0)  # Add batch dimension (1, 224, 224, 3)

# Define the prediction endpoint
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Read uploaded file contents
        contents = await file.read()

        # Open image from byte stream and ensure it's RGB format
        img = Image.open(io.BytesIO(contents)).convert("RGB")

        # Preprocess image to match model input
        input_data = preprocess(img)

        # Make prediction using the model
        prediction = model.predict(input_data)

        # Get class with highest confidence score
        predicted_class = class_names[np.argmax(prediction)]

        # Get the confidence score (maximum probability)
        confidence = float(np.max(prediction))

        # Return prediction result
        return {"class": predicted_class, "confidence": confidence}

    # Handle case when uploaded file is not a valid image
    except UnidentifiedImageError:
        return {"error": "Prediction failed: cannot identify image file"}

    # Handle other exceptions
    except Exception as e:
        return {"error": f"Prediction failed: {str(e)}"}
