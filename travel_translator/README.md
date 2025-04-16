# AI Language Translator for Travelers

An AI-powered language translation application designed specifically for travelers. This Streamlit app provides real-time translations, conversation assistance, and common travel phrases in multiple languages.

## Features

- **Text Translation**: Translate text between multiple languages
- **Conversation Mode**: Interactive chat interface for simulated conversations
- **Common Travel Phrases**: Access to pre-translated common phrases by category
- **Pronunciation Guides**: Optional pronunciation help for better communication
- **Voice Output**: (Simulated) Text-to-speech capability

## Setup and Installation

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create the required folders:
   ```
   mkdir -p static
   ```
4. Add a logo image to the static folder (optional)
5. Run the application:
   ```
   streamlit run app.py
   ```

## Project Structure

- `app.py`: Main Streamlit application
- `translator.py`: Translation functionality
- `static/`: Static files (CSS, images)
  - `style.css`: Custom styling
  - `logo.png`: App logo
- `requirements.txt`: Project dependencies
- `README.md`: Project documentation

## Implementation Notes

This is a prototype version with simulated translations. In a production environment, you would need to:

1. Connect to a real translation API (Google Cloud Translation, Azure Translator, DeepL, etc.)
2. Add proper error handling and rate limiting
3. Implement actual text-to-speech functionality
4. Add user authentication if needed
5. Set up proper data storage for user history and preferences

## Future Enhancements

- Image-based translation (take a photo of text and translate)
- Offline translation capability
- Voice input for hands-free operation
- Cultural notes and travel tips
- Save favorite phrases for quick access
- Location-based phrase suggestions