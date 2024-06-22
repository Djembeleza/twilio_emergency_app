from logging.config import dictConfig
from collections import namedtuple
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

Response = namedtuple("Response", ['text'])

@app.route('/')
def whats_good():
    return render_template('landing_page.html')

@app.route('/sms', methods=["POST"])
def hello():
    model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=read_file('prompts/emergency.txt'))

    chat_history = session.get(request.values.get("From"), [])

    body = request.values.get('Body', None)
    messages = chat_history
    messages.append({
        "role": "user",
        'parts': [body]
    })

    if "end convo" not in body:
        res = model.generate_content(messages)
    else:
        res = Response("Thank you. Always here to give you a hand.")

    messages.append({
        'role': "model",
        'parts': [res.text]
    })

    if "end convo" not in body:
        session[request.values.get("From")] = messages
    else:
        session.pop(request.values.get('From'), None)

    response = MessagingResponse()
    response.message(res.text)

    return str(response)



if __name__ == '__main__':
    app.run(debug=True, port=3000)