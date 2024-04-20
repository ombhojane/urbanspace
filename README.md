## How to Setup

To run the Urban Space app locally, follow these steps:

1. **Install Dependencies**: Install the required libraries by running the following command:
   
   pip install -r requirements.txt

2. **Set up Environment Variables**: Create a `.env` file in the project's root directory and replace the `GENAI_API_KEY` placeholder with your actual Gemini API key:
   
   GENAI_API_KEY=your_gemini_api_key

3. **Run the App**: Start the Flask app by running the following command:
   
   python app.py

This will start the app on `http://127.0.0.1:5000/` in your local environment.
