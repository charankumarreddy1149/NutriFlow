from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to get Gemini Vision API response using the updated model
def get_gemini_response(image_parts, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt, image_parts[0]])
    return response.text

# Function to process uploaded image or camera input
def input_image_setup(uploaded_file, camera_input):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }]
        return image_parts
    elif camera_input is not None:
        bytes_data = camera_input.getvalue()
        image_parts = [{
            "mime_type": "image/jpeg",  # Assuming JPEG for camera input
            "data": bytes_data
        }]
        return image_parts
    else:
        raise FileNotFoundError("No image uploaded or captured.")

# Set up Streamlit UI
st.set_page_config(page_title="NutriAi", page_icon="🥘", layout="wide")

# Centered Title using HTML
st.markdown("<h1 style='text-align: center;'>NutriFlow: Personalized Meal Planning & Analysis</h1>", unsafe_allow_html=True)

# Tabs for analysis and meal plan
analyze_tab, plan_tab = st.tabs(["📊 Analyze Meal", "📋 Personalized Meal Plan"])

with analyze_tab:
    col1, col2 = st.columns([2, 1])
    with col1:
        # File uploader
        uploaded_file = st.file_uploader("📤 Upload your delicious meal photo...", type=["jpg", "jpeg", "png"])
        # Camera input
        camera_input = st.camera_input("📸 Take a picture of your meal...")

        # Additional prompt for food preparation details
        prep_prompt = st.text_input("Tell us how your meal was prepared (e.g., grilled, fried, steamed) for a more detailed analysis:")
        # Analyze Button
        analyze_clicked = st.button("🍽️ Analyze My Meal")

    with col2:
        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, caption="📸 Uploaded Meal", use_column_width=True, output_format="JPEG", width=300)
            st.markdown(
                """
                <style>
                img {
                    height: 200px !important;
                    object-fit: contain;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
        elif camera_input:
            image = Image.open(camera_input)
            st.image(image, caption="📸 Captured Meal", use_container_width=True, output_format="JPEG", width=300)
            st.markdown(
                """
                <style>
                img {
                    height: 200px !important;
                    object-fit: contain;
                }
                </style>
                """,
                unsafe_allow_html=True
            )


    # Base Nutrition prompt
    base_prompt = """
    You are an expert nutritionist. Analyze the food items from the image and calculate total calories.
    Provide the analysis in this format:

    FOOD ITEMS AND CALORIES:
    1. Item 1 - XXX calories
    2. Item 2 - XXX calories
    3. Item 3 - XXX calories

    TOTAL CALORIES:
    Your total caloric intake from this meal is XXX calories.

    NUTRITIONAL ANALYSIS:
    - Carbohydrates: XX%
    - Protein: XX%
    - Fat: XX%

    RECOMMENDATION:
    [Your food is healthy/Your food is not healthy] because [reason].
    Suggested improvements: [suggestions].
    """

    # Append preparation details to the base prompt if provided
    input_prompt = base_prompt + ("\nMeal Preparation Details: " + prep_prompt if prep_prompt else "")

    if (uploaded_file or camera_input) and analyze_clicked:
        with st.spinner("🔍 Analyzing your meal..."):
            try:
                image_data = input_image_setup(uploaded_file, camera_input)
                response = get_gemini_response(image_data, input_prompt)
                st.subheader("🧠 Nutritional Analysis:")
                st.write(response)
            except Exception as e:
                st.error(f"Something went wrong: {e}")

with plan_tab:
    st.subheader("🍽️ Generate a Personalized Meal Plan")
    diet_preferences = st.text_input("Enter your food preferences (e.g., vegetarian, low-carb, gluten-free, etc.):")
    if st.button("Generate Meal Plan"):
        with st.spinner("Creating your personalized meal plan..."):
            try:
                meal_plan_prompt = f"Generate a detailed 7-day personalized meal plan based on the following preferences: {diet_preferences}. Include recipes, nutritional information, and grocery list."
                model = genai.GenerativeModel('gemini-1.5-flash')
                meal_plan_response = model.generate_content(meal_plan_prompt)
                st.subheader("Your 7-Day Personalized Meal Plan:")
                st.write(meal_plan_response.text)

                st.download_button(
                    label="Download Meal Plan 📄",
                    data=meal_plan_response.text,
                    file_name="personalized_meal_plan.txt",
                    mime="text/plain"
                )
            except Exception as e:
                st.error(f"Something went wrong: {e}")
