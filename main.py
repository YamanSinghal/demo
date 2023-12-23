import sys
# sys.path.append("../")
import streamlit as st
# import pyaudio
import wave
from chatbot.audio_chat import AudioChatApp
from chatbot.text_chat import TextChatApp
# Initialize the AudioChatApp and TextChatApp
audio_chat_app = AudioChatApp()
text_chat_app = TextChatApp()


# FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 5

st.set_page_config(
    page_title="Strangify",
    page_icon="strangify.jpeg"  # Replace with the actual URL of your logo
)
st.title("Strangify")

# Create the sidebar with settings
st.sidebar.header("Limitless support , One platform")
st.sidebar.image("strangify.jpeg", use_column_width=True)
st.sidebar.markdown("<small>Powered by Strangify</small>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

input_message = st.text_input("What is up?", key="input_message")
recording = False

if st.button("Send", key="send_button"):
    response = text_chat_app.chat(input_message)
    st.session_state.messages.append({"role": "strangify", "content": response})

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.empty():
        role = message['role']
        content = message['content']
        st.write(f"{role}: {content}")