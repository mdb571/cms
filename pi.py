import serial
import RPi.GPIO as GPIO
import time
from twilio.rest import Client
from twilio import twiml
from dotenv import load_dotenv

load_dotenv()

client = Client(ACCOUNT_SID,AUTH_TOKEN)



ser=serial.Serial("/dev/ttyUSB0",9600)  

while True:
    read_ser=ser.readline().decode("utf-8")
    print(read_ser)