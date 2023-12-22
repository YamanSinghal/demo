import openai
import os
from utils.prompt import PROMPT_FOR_GPT


openai.api_key = "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"

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
