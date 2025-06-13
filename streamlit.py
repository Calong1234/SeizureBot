import streamlit as st
import os
from dotenv import load_dotenv
import google.genai as genai

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
telegram_token = os.getenv("TELEGRAM_TOKEN")
telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")
client = genai.Client(api_key=gemini_api_key)
run = True

st.title("⚠️Seizure Assistant Helpbot⚠️")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    name = message[0]
    frame = message[1]
    st.chat_message(name=name).write(f"{frame}")

user_input = st.chat_input(placeholder="Enter your message here")
if user_input == None:
    user_input = "Help! Someone is having a seizure!"
    run = True

if run == True:
    st.chat_message("user").write(user_input)
    st.session_state.chat_history.append(["user", user_input])
    if user_input == "Help! Someone is having a seizure!":
        user_input += "Your first response has to be instructions on how to help someone having a seizure. Keep your instructions concise."
    ml_response = client.models.generate_content(
    model="gemini-2.0-flash",
    config=genai.types.GenerateContentConfig(system_instruction="you are a Ai helpbot for seizure help in Singapore."),
    contents=user_input)
    response = ml_response.text

    st.session_state.chat_history.append(["ai", response])
    st.chat_message("ai").write(response)
    run = False