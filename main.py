import sys
import streamlit as st
from chatbot.audio_chat import AudioChatApp
from chatbot.text_chat import TextChatApp

# Initialize the AudioChatApp and TextChatApp
audio_chat_app = AudioChatApp()
text_chat_app = TextChatApp()
# st.write("Secret Key", st.secrets["openai_secret_key"])

# Set up Streamlit page configuration
st.set_page_config(
    page_title="Strangify",
    page_icon="/home/drono07/chat_bot_demo/chat_bot_demo/strangify.jpeg"
)

# Set up Streamlit sidebar
st.sidebar.header("Limitless support, One platform")
st.sidebar.image("/home/drono07/Desktop/strangify/strangify.jpeg", use_column_width=True)
st.sidebar.markdown("<small>Powered by Strangify</small>", unsafe_allow_html=True)

# Initialize messages in session state if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to send a message
def send_message():
    input_message = st.session_state.input_message
    response = text_chat_app.chat(input_message)
    st.session_state.messages.append({"role": "strangify", "content": response})
    
    # Clear the input message after sending
    st.session_state.input_message = ""

# Display title
st.title("Strangify")

# Create the sidebar with settings

# Input for text messages
st.text_input("What is up?", key="input_message", on_change=send_message)

# Button to send messages
if st.button("Send", key="send_button"):
    send_message()

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.empty():
        role = message['role']
        content = message['content']
        st.write(f"{role}: {content}")

# JavaScript to simulate a click on the "Send" button when Enter is pressed
js_code = """
document.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        document.getElementById("send_button").click();
    }
});
"""
st.markdown(f"<script>{js_code}</script>", unsafe_allow_html=True)