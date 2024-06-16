from flask import Flask, request, jsonify
from chatbot import get_chatbot_response
from translator import translate_text

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data['message']
    user_language = data.get('language', 'en')

    # Translate message to English (if necessary)
    translated_message = translate_text(user_message, source_lang=user_language, target_lang='en')
    
    # Get chatbot response
    response = get_chatbot_response(translated_message, language=user_language)
    
    # Translate response back to user's language (if necessary)
    final_response = translate_text(response, source_lang='en', target_lang=user_language)

    return jsonify({'response': final_response})

if __name__ == '__main__':
    app.run(debug=True)
