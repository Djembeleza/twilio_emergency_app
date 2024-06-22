from logging.config import dictConfig
import google.generativeai as genai

from twilio.twiml.messaging_response import MessagingResponse

from flask import (
    Flask,
    request,
    render_template,
    session
)

from dotenv import dotenv_values

from utils.util import (
    read_file
)

config = dotenv_values('.env')

genai.configure(
    api_key=config["GOOGLE_API_KEY"]
)

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


app = Flask(__name__)
app.secret_key = config["SECRET_KEY"]
app.config.from_object(__name__)

@app.route('/')
def whats_good():
    return "<h1>What's goood, nyigga !</h1>"

@app.route('/sms', methods=["POST"])
def hello():
    model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=read_file('prompts/emergency.txt'))

    chat_history:list = session.get(request.values.get("From"), [
      
    ])
    body = request.values.get('Body', None)
    
    messages = chat_history
    
    messages.append({
        "role": "user",
        'parts': [body]
    })

    res = model.generate_content(messages) if "end convo" not in body else {'text': "Thank you. Always here to give you a hand."}

    messages.append(
        {
            'role': "model",
            'parts': [res.text]
        }
    )

    print(
        session
    )

    if "end convo" not in body:

        session[request.values.get("From")] = messages
    else:
        session.pop(
            request.values.get('From'),
            None
        )

    response = MessagingResponse()
    response.message(res.text)
    return str(response)


if __name__ == '__main__':
    app.run(debug=True, port=3000)