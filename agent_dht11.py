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

url = 'http://10.1.2.143:5000/send'
# 'https://lsbu-sensors.herokuapp.com/send'


def send_data(payload):
    r = requests.get(url, params=payload)
    data = json.loads(r.content.decode("utf-8"))
    print(data)


def get_data():
    result = instance.read()
    if result.is_valid():
        print("Temp: %d C" % result.temperature +' '+"Humid: %d %%" % result.humidity)
        payload = {'temperature': result.temperature, 'humidity': result.humidity}
        try:
            send_data(payload)
        except Exception as e:
            print('Error', e)


if __name__ == '__main__':
    while True:
        get_data()
        time.sleep(1)
