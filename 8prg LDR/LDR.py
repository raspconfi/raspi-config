from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)

@app.route("/")
def index():
    light_level = GPIO.input(18)
    if light_level:
        label = "Dark"
    else:
        label = "Bright"
    templateData = {
        'light_level': label
    }
    return render_template('index.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
