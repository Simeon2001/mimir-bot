import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("GPT_KEY")

messages=[]
messages.append( {"role": "system", "content": "you are a bot named mimir, you are designed to provide people with intelligent and insigntful responses to questions and requests."})
def answer(msg):
    try:
        messages.append(
                {"role": "user", "content": msg}
            )
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages= messages
        )

        response = (completion.choices[0].message)
        messages.append({"role": "assistant", "content": response["content"]})
        return response["content"]
    
    except:
        msg = "my brain is currently snoozing"
        return msg

