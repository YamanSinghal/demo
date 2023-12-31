import openai
import os
from utils.prompt import PROMPT_FOR_GPT
from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st

# Set OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["openai_secret_key"]

st.write("Secret Key", st.secrets["openai_secret_key"])

class TextChatApp:
    def __init__(self):
        self.messages = [
            {"role": "system", "content": PROMPT_FOR_GPT}
        ]

    def chat(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        
        # Set parameters for OpenAI API call
        params = {
            "model": "gpt-3.5-turbo",
            "messages": self.messages,
            "max_tokens": 100,  # Set the maximum token length
            "temperature": 1.0,  # Set the temperature for sampling
        }

        response = openai.ChatCompletion.create(**params)
        chatgpt_reply = response["choices"][0]["message"]["content"]
        self.messages.append({"role": "assistant", "content": chatgpt_reply})

        chat_transcript = ""
        for message in self.messages:
            if message['role'] == 'user':
                chat_transcript += message['content'] + "\n\n"
        chat_transcript += chatgpt_reply + "\n\n"

        return chat_transcript