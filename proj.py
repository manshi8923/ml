import streamlit as st
import os
import google.generativeai as genai
os.environ["GOOGLE_API_KEY"]="AIzaSyBz6eeMz-o8K1mIlv2X2fHkZV4m8pZN-5w"
genai.configure(api_key="GOOGLE_API_KEY")
## function to load gemini pro model and get response
model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])
def get_gemini_response(question):
  response=chat.send_message(question,stream=True)
  return response

## initialise our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")
## initialise our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini LLM Application")

## initialise global variable for chat history
if 'chat_history' not in globals():
    chat_history = []

input_text = st.text_input("Input: ", key="input")
submit_button = st.button("Ask the questions")
if submit_button and input_text:
    response = get_gemini_response(input_text)
    # Add user query and response to chat history
    chat_history.append(("You", input_text))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        chat_history.append(("Bot", chunk.text))

st.subheader("The Chat History is")
for role, text in chat_history:
    st.write(f"{role}: {text}")