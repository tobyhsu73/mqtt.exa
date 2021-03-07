import paho.mqtt.client as mqtt #import the client1
import time
############
def on_message(client, userdata, message):
    print(str(message.payload.decode("utf-8")),\
          "topic",message.topic,)
    if message.retain==1:
        print("This is a retained message")
########################################
broker_address="192.168.0.111"
#broker_address="iot.eclipse.org"
while True:
    client = mqtt.Client("P1") #create new instance
    client.on_message=on_message #attach function to callback

    client.connect(broker_address) #connect to broker
    client.loop_start() #start the loop

    client.subscribe("test/hehe")


    time.sleep(4) # wait
    client.loop_stop() #stop the loop
