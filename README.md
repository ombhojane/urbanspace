# Urban Space

Urban Space is designed to address the lack of accessible green spaces in urban areas. Our goal is to transform vacant urban spaces into vibrant green havens, promoting a healthier and more sustainable urban environment.

## Features

1. **City Map Exploration**: Users can enter their city and obtain a map, allowing them to pan, zoom, and capture images of desired city areas.

2. **Vacant Space Identification**: By uploading city images, our platform analyzes the imagery and identifies vacant spaces suitable for green space development. It provides details about these spaces, including plans for their transformation into green havens, considering factors such as current features, geographic conditions, and accessibility.

3. **Green Space Visualization**: Users can upload images of specific land areas, and our platform generates visual simulations showcasing how the green space would look after implementation.

## How to Setup

To run the Urban Space app locally, follow these steps:

1. **Install Dependencies**: Install the required libraries by running the following command:
   
   pip install -r requirements.txt

2. **Set up Environment Variables**: Create a `.env` file in the project's root directory and replace the `GENAI_API_KEY` placeholder with your actual Gemini API key:
   
   GENAI_API_KEY=your_gemini_api_key

3. **Run the App**: Start the Flask app by running the following command:
   
   python app.py

This will start the app on `http://127.0.0.1:5000/` in your local environment.


## Technologies Used

- **Backend**: Flask
- **Frontend**: HTML with Tailwind CSS, Js, Streamlit (for testing)
- **Mapping**: Maptiler API, Geopy
- **Vacant Space Identification**: Prompt-tuned Gemini LLM
- **Green Space Visualization**: Fine-tuned ControlNet Stable Diffusion model
- **Deployment**: Vercel
