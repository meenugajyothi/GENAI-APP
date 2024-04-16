from openai import OpenAI
import streamlit as st

# Read the API Key and setup an OpenAI Client
f = open("keys/.openai_api_key.txt")
key = f.read()
client = OpenAI(api_key = key)
st.snow()
st.title(" GenAI MCQ")
st.header('MCQ GENERATOR APP')

# Take User's input
prompt = st.text_input('Enter a data science topic')

# if the button is clicked, genarate responses

if st.button("Genarate") == True:
    st.balloons()
    
    response = client.chat.completions.create(
       model="gpt-3.5-turbo",
        messages=[
            {"role":"system","content": """AI Assistant"
                                         
                                            Given a Data Science topic yiu always Generate 6 data Science questions and answer for MCQ test in MCQ format."""},
            {"role":"user","content":prompt}
            ]


    )

    # print the response on the web app 
    if response.choices:
        st.write(response.choices[0].message.content)