import os
import openai
from utils.prompt import PROMPT_FOR_GPT


# openai.api_key = "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"

class AudioChatApp:
    def __init__(self):
        self.messages = [{"role": "system", "content": PROMPT_FOR_GPT}]

    def transcribe(self, audio):
        audio_filename_with_extension = audio

        audio_file = open(audio_filename_with_extension, "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)

        user_message = {"role": "user", "content": transcript["text"]}
        self.messages.append(user_message)

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=self.messages,max_tokens = 100)

        response = response["choices"][0]["message"]["content"]

        return f"User: {user_message['content']} \n Strangify: {response}"



