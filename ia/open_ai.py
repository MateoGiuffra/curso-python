import requests 
import json 
import os 
from dotenv import load_dotenv

load_dotenv()
OPEN_AI_KEY = os.environ['OPEN_AI_KEY']

def call_open_ai():
    try: 
        prompt = input("Escribe un mensaje:\n")
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {OPEN_AI_KEY}"
        }
        data = {
            "model": "gpt-4o-mini",
            "messages": [{
                "role": "user", 
                "content": prompt
            }]
        }
        response = requests.post(url, json=data, headers=headers)
        json_api_response = response.json()
        print(json_api_response)
    except Exception as e: 
        print(e)


def start_chat():
    while(True): 
        call_open_ai()
        