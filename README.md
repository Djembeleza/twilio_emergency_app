# twilio_emergency_app
An application that uses Twilio API to give users with feature phones access to emergency services

With this application, users should be able to request information about certain emergencies using SMS or Voice Call

Depending on the severity of the emergency, the application can have following up conversation using certain **urgent** keywords.

The application should have a landing page with basic information on what it's about, contributors and instructions on how can people use it.

## Resources

### Backend
- [Flask](https://flask.palletsprojects.com/en/3.0.x/) - We'll be using Flask to create a webhook that checks content of the sms or voicecall
- [Twilio Programmable Messaging API](https://www.twilio.com/docs/messaging) - We'll be using Twilio to process incoming SMS. We'll be using *[Receive and Reply to Incoming Messages - Python](https://www.twilio.com/docs/messaging/tutorials/how-to-receive-and-reply/python)* as a reference on processing incoming messages. 
- For creating conversations, we'll be using the *[Create an SMS Conversation in Python](https://www.twilio.com/docs/messaging/tutorials/how-to-create-sms-conversations/python)* to implement conversations during severe situations
- We'll be using *[Respond to Incoming Phone Calls in Python](https://www.twilio.com/docs/voice/tutorials/how-to-respond-to-incoming-phone-calls/python)* to process incoming calls. Since this application is for emergencies, we'll be using *[How to Record Phone Calls in Python](https://www.twilio.com/docs/voice/tutorials/how-to-record-phone-calls/python)* to record conversations in severe cases
- For AI, we'll be using [Google Gemini AI](https://ai.google.dev/)

### Frontend
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML) for the structure of the landing page
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS) for styling
- [Bootstrap 5](https://getbootstrap.com/) for faster development, responsiveness
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference) for some functionalities
- [D3.js](https://d3js.org/) for displaying some of the visual data

## Installation
1. Clone the repository

    `git clone https://github.com/Djembeleza/twilio_emergency_app`
2. Cd into the project

    `cd twilio_emergency_app`
3. Create virtual environment

    `python3 -m venv env`
4. Activate environment

    `source env/bin/activate`
5. Install the required packages

    `pip install -r requirements.txt`
1. Rename the example.env to add your environment varibles
   
   `mv example.env .env`

2. To run the application
   
   `python app.py`