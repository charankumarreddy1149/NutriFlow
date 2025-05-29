🥘 NutriAi - AI Meal Analyzer
NutriAi is an intelligent web application that leverages the power of Google's Gemini Vision AI to analyze meal photos, provide nutritional breakdowns, and generate personalized meal plans based on user preferences. Whether you want to quickly understand the caloric content of your food or get a full 7-day diet plan, NutriAi has you covered.

✨ Features
Meal Photo Analysis: Upload a photo of your meal or capture one using your camera to get a detailed nutritional analysis.

Calorie Estimation: Automatically estimates the total calories and provides a breakdown of individual food items and their caloric content.

Nutritional Breakdown: Offers a percentage-based analysis of carbohydrates, protein, and fat.

Dietary Recommendations: Provides insights into the healthiness of your meal and suggests improvements.

Preparation Details Input: Allows you to input how your meal was prepared (e.g., grilled, fried, steamed) for more accurate analysis.

Personalized Meal Plans: Generate a customized 7-day meal plan based on your dietary preferences (e.g., vegetarian, low-carb, gluten-free).

Downloadable Meal Plans: Download your generated meal plan as a text file for offline access.

Interactive User Interface: A clean and user-friendly interface powered by Streamlit.

🚀 Technologies Used
Streamlit: For building the interactive web application.

Google Generative AI (Gemini API): The core AI model for image analysis and meal plan generation.

Python-dotenv: For securely loading environment variables (API key).

Pillow (PIL): For image processing.

🛠️ Setup Instructions
Follow these steps to set up and run NutriAi on your local machine:

1. Clone the Repository
git clone <repository_url>
cd <repository_folder>

(Replace <repository_url> and <repository_folder> with your actual repository URL and the folder name after cloning.)

2. Create a Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate  # On Windows: `venv\Scripts\activate`

3. Install Dependencies
Install the required Python packages using pip:

pip install -r requirements.txt

4. Set Up Your Google API Key
Go to the Google AI Studio and generate a new API key.

Create a file named .env in the root directory of your project (the same directory as app2.py).

Add your Google API key to the .env file in the following format:

GOOGLE_API_KEY="YOUR_API_KEY_HERE"

Replace "YOUR_API_KEY_HERE" with the actual API key you obtained.

5. Run the Application
streamlit run app2.py

This command will open the NutriAi application in your default web browser.

📝 How to Use
Analyze Meal Tab:
Upload Photo: Click "📤 Upload your delicious meal photo..." to upload an image from your device.

Take Photo: Alternatively, click "📸 Or take a picture of your meal..." to use your device's camera.

Preparation Details (Optional): Enter how your meal was prepared (e.g., "grilled," "steamed") in the text box for a more precise analysis.

Analyze: Click the "🍽️ Analyze My Meal" button. The AI will process the image and display the nutritional analysis.

Personalized Meal Plan Tab:
Enter Preferences: Type in your dietary preferences (e.g., "vegetarian, low-carb, gluten-free") in the input field.

Generate Plan: Click the "Generate Meal Plan" button. The AI will create a detailed 7-day meal plan.

Download Plan: Once the plan is generated, click "Download Meal Plan 📄" to save it as a text file.

🔮 Future Enhancements
Integration with a database to save user history and meal plans.

User authentication for personalized dashboards.

More advanced nutritional tracking and goal setting.

Integration with food databases for more precise item recognition.

Voice input for meal preparation details.
