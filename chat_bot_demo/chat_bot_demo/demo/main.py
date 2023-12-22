import sys
sys.path.append("../")
import streamlit as st
import pyaudio
import wave
from chatbot.audio_chat import AudioChatApp
from chatbot.text_chat import TextChatApp
# Initialize the AudioChatApp and TextChatApp
audio_chat_app = AudioChatApp()
text_chat_app = TextChatApp()


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
CHUNK = 1024
RECORD_SECONDS = 5

# Function to record audio
def record_audio():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    # st.text("Recording...")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    p.terminate()

    # Save the recorded audio as a WAV file
    audio_filename = "recorded_audio.wav"
    wf = wave.open(audio_filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    return audio_filename

st.set_page_config(
    page_title="BOT",
)
st.title("BOT")

# Create the sidebar with settings
st.sidebar.header("Limitless support , One platform")

if "messages" not in st.session_state:
    st.session_state.messages = []

input_message = st.text_input("What is up?", key="input_message")

recording = False

if st.button("Send", key="send_button"):
    response = text_chat_app.chat(input_message)
    st.session_state.messages.append({"role": "xyz", "content": response})

if st.button("Record"):
    audio_filename = record_audio()
    st.audio(audio_filename, format="audio/wav")
    recording = True


if recording:
    chat_transcript = audio_chat_app.transcribe(audio_filename)
    st.write(chat_transcript)  


# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.empty():
        role = message['role']
        content = message['content']
        st.write(f"{role}: {content}")