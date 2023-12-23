import openai
import os
from utils.prompt import PROMPT_FOR_GPT
from dotenv import load_dotenv
load_dotenv()
import os

openai.api_key = os.getenv('KEY')

class TextChatApp:
    def __init__(self):
        self.messages = [
            {"role": "system", "content": PROMPT_FOR_GPT}
        ]

    def chat(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        chatgpt_reply = response["choices"][0]["message"]["content"]
        self.messages.append({"role": "assistant", "content": chatgpt_reply})

        chat_transcript = ""
        for message in self.messages:
            if message['role'] == 'user':
                chat_transcript += message['content'] + "\n\n"
        chat_transcript += chatgpt_reply + "\n\n"

        return chat_transcript
