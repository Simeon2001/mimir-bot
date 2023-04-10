from urllib import response
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("GPT_KEY")


def answer(msg):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "assistant", "content": msg}
            ]
        )

        response = (completion.choices[0].message)
        
        return response["content"]
    
    except:
        msg = "my brain is currently snoozing"
        return msg
