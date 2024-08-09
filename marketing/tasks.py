# myapp/tasks.py
from celery import shared_task
from DrissionPage import ChromiumPage, ChromiumOptions
import pyperclip
from groq import Groq

@shared_task
def process_user_input(text):
    client = Groq(
        api_key="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",
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": text,
            }
        ],
        model="llama3-8b-8192",
    )
    result =  chat_completion.choices[0].message.content
    print(result)
    return  result

# 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