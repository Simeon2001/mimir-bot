from urllib import response
import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("GPT_KEY")


def answer(msg):

    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=msg,
        temperature=0.2,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    replyit = response["choices"][0]["text"]
    return replyit
