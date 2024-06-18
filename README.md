# twilio_emergency_app
An application that uses Twilio API to give users with feature phones access to emergency services

With this application, users should be able to request information about certain emergencies using SMS or Voice Call

Depending on the severity of the emergency, the application can have following up conversation using certain **urgent** keywords.

The application should have a landing page with basic information on what it's about, contributors and instructions on how can people use it.

## Resources
### Backend
- [Flask](https://flask.palletsprojects.com/en/3.0.x/) - We'll be using Flask to create a webhook that checks content of the sms or voicecall
- Twilio 