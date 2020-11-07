import serial
import RPi.GPIO as GPIO
import time
from twilio.rest import Client
from twilio import twiml
from dotenv import load_dotenv
import os
import requests

load_dotenv()
ACCOUNT_SID=os.environ.get('ACCOUNT_SID')
AUTH_TOKEN=os.environ.get('AUTH_TOKEN')
client = Client(ACCOUNT_SID,AUTH_TOKEN)



ser=serial.Serial("/dev/ttyUSB1",9600)  

def get_data():
    prev_count=0
    while True:
        read_ser=int(ser.readline().decode("utf-8"))
        print(read_ser)
        if read_ser>5:
            send_msg()
            prev_count=0
        if read_ser!=prev_count:
            requests.post('https://my2ujg.deta.dev/update/'+str(read_ser))
            prev_count=read_ser
        
        


def send_msg():
    message = client.messages \
                    .create(
                        body="Dear User\n,There are more numbers of persons in your hall than what is allowed! Please consider following proper government guidelines.!",
                        from_=os.environ.get('FROM'), #use your twilio no here
                        to=os.environ.get('TO'), #use your verified phone no. here
                    )
    
get_data()