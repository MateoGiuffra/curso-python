import requests 
import json 
import os 
from dotenv import load_dotenv

load_dotenv()
DEEPSEEK_KEY = os.environ['DEEPSEEK_KEY']

def call_deepseek():
    try: 
        prompt = input("Escribe un mensaje:\n")
        url = "https://api.deepseek.com/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {DEEPSEEK_KEY}"
        }
        data = {
            "model": "deepseek-chat",
            "messages": [{
                "role": "user", 
                "content": prompt
            }]
        }
        response = requests.post(url, json=data, headers=headers)
        json_api_response = response.json()
        print(json_api_response)
    # print(json_api_response["choices"][0]["message"]["content"])
    except Exception as e: 
        print(e)


def start_chat():
    while(True): 
        call_deepseek()
        
call_deepseek()
    