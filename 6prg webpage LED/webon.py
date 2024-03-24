import RPi.GPIO as GPIO
from flask import Flask, render_template

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

@app.route("/")
def index():
    templateData = {
        'title' : 'LED Control'
    }
    return render_template('index.html', **templateData)

@app.route("/led/<action>")
def action(action):
    if action == "on":
        GPIO.output(18, True)
    if action == "off":
        GPIO.output(18, False)
    templateData = {
        'title' : 'LED Control',
        'led_state': action
    }
    return render_template('index.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=7000, debug=True)

