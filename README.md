# PolyglotBot

PolyglotBot is a multilingual chatbot that can understand and respond in multiple languages. This project showcases an integration of AI-powered chatbot functionality with a simple web interface.

## Project Structure

- `chatbot.py`: Contains the chatbot logic.
- `translator.py`: Handles the translation of messages to and from the chatbot's operating language.
- `index.html`, `style.css`, `script.js`: Web interface files for interacting with the chatbot.
- `server.py`: Flask server to handle requests and integrate the chatbot and translation components.

## Setup

1. Ensure you have Python installed on your system.
2. Install Flask: `pip install flask`
3. To run the server: `python server.py`
4. Open `index.html` in a web browser to interact with the chatbot.

## Note

This is a simplified example intended for educational purposes. For a production system, please integrate a robust NLP model and a reliable translation service.
