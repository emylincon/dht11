import RPi.GPIO as GPIO
import dht11
import time
import requests
import json

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()

# read data using Pin GPIO21
instance = dht11.DHT11(pin=21)


def send_data(payload):
    r = requests.get('http://127.0.0.1:5000/ticker', params=payload)
    data = json.loads(r.content)
    print(data)


def get_data():
    result = instance.read()
    if result.is_valid():
        print("Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity)
        payload = {'temperature': result.temperature, 'pressure': result.humidity}
        send_data(payload)


if __name__ == '__main__':
    while True:
        get_data()
        time.sleep(1)