import google.generativeai as genai

from twilio.twiml.messaging_response import MessagingResponse

from flask import (
    Flask,
    request,
    render_template,
    session
)

from dotenv import dotenv_values

config = dotenv_values('.env')

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def whats_good():
    return "<h1>What's goood, nyigga !</h1>"

@app.route('/sms', methods=["POST"])
def hello():
    model = genai.GenerativeModel("gemini-1.5-flash")

    chat_history:list = session.get(request.values.get("From"), [])
    body = request.values.get('Body', None)
    
    messages = chat_history
    
    messages.append({
        "role": "user",
        'parts': [body]
    })

    res = model.generate_content(messages)

    messages.append(
        {
            'role': "model",
            'parts': [res.text]
        }
    )

    session[request.values.get("From")] = messages

    response = MessagingResponse()
    response.message(res.text)
    return str(response)


if __name__ == '__main__':
    app.run(debug=True, port=3000)