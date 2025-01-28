# subscriber.py
import paho.mqtt.client as mqtt
import time
import json

from gemini_ai_call import * 
from gemini_myapi import *

# 0. Importing the necessary functions for the Gemini API LLM Interaction to Work
def __get_gemini_client__() -> genai.GenerativeModel:
    genai.configure(api_key=the_api_key)
    gemini_model = genai.GenerativeModel("gemini-1.5-flash")
    return gemini_model

gemini_model = __get_gemini_client__()


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Successfully connected to broker")
        # Subscribe to topic
        client.subscribe("gemini_llm_test/uscolleges/schdetails")
    else:
        print(f"Connection failed with code {rc}")

def on_message(client, userdata, msg):
    # 1. Receive and decode the MQTT message
    received_message = msg.payload.decode()
    print("\nA. Message Payload From Developed JSON file via a subscription topic:\n", received_message, "\n")

    # 2. Create a prompt for the Gemini API
    prompt = f"Generate a summary analysis of this school and its corresponding data for a student willing to go to college in the US. Here is the information: {received_message}"

    # 3. Call the Gemini API
    try:
        response = gemini_model.generate_content(prompt).text
        print("\nB. Gemini LLM Response:\n")
        for line in response.split("\n"):
            print(f"  - {line}")
        print("\n")
        
        # Saving only the response to a JSON file as context for future LLM interactions
        with open("llm_responses.json", "a") as f:
            json.dump(response, f, indent=4)
            f.write("\n") 
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        
    # 4. Separator
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

# Create subscriber client
subscriber = mqtt.Client()
subscriber.on_connect = on_connect
subscriber.on_message = on_message

# Connect to public broker
print("Connecting to broker...")
subscriber.connect("test.mosquitto.org", 1883, 60)

# Start the subscriber loop
subscriber.loop_start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping subscriber...")
    subscriber.loop_stop()
    subscriber.disconnect()