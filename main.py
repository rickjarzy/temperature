import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4     # GPIO Pin responsible for data connection and transfer

while True:
    hum, temp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if hum is not None and temp is not None:
        print("Temperature: {0:0.1f} C° - Luftfeuchte= {1:0.1f}%".format(temp, hum))
    else:
        print("No Sensor data is availiable")

    time.sleep(1)
