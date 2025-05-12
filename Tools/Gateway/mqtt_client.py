import os
import paho.mqtt.client as mqtt
from dotenv import load_dotenv

load_dotenv()

AIO_USER = os.getenv("AIO_USERNAME")
AIO_KEY = os.getenv("AIO_KEY")
AIO_HOST = os.getenv("AIO_HOST", "io.adafruit.com")
AIO_PORT = int(os.getenv("AIO_PORT", 1883)) # hoặc thử gọi 8883 nếu ko kết nối đc

AIO_FEED_IDs = ["1", "Failure", "Unknow"]

    
client = mqtt.Client()
client.username_pw_set(AIO_USER, AIO_KEY)
client.connect(AIO_HOST, AIO_PORT, 60)
#client.loop_start() 
#loop

def publish_result(result: str):
    # Reset all
    client.publish("nhatminh1710/feeds/1", "0")
    client.publish("nhatminh1710/feeds/Failure", "0")
    client.publish("nhatminh1710/feeds/Unknow", "0")

    if result == "success":
        client.publish("nhatminh1710/feeds/1", "1")
    elif result == "failure":
        client.publish("nhatminh1710/feeds/Failure", "1")
    else:
        client.publish("nhatminh1710/feeds/Unknow", "1")
