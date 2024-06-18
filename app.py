from flask import (
    Flask,
    request,
    render_template
)

from dotenv import dotenv_values

config = dotenv_values('.env')

app = Flask(__name__)

@app.route('/')
def whats_good():
    return "<h1>What's goood, nyigga !</h1>"

if __name__ == '__main__':
    app.run(debug=True, port=3000)