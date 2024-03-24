import RPi.GPIO as GPIO
import time
import Adafruit_GPIO.I2C as I2C

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
sensor_pin = 18
buzzer_pin = 17
GPIO.setup(sensor_pin, GPIO.IN)
GPIO.setup(buzzer_pin, GPIO.OUT)
one=1
while True:
    sensor_value = GPIO.input(sensor_pin)
    if sensor_value==one:
        GPIO.output(buzzer_pin, False)
        print(sensor_value)
    else:
        GPIO.output(buzzer_pin, True)
        time.sleep(1)
        print(sensor_value)

