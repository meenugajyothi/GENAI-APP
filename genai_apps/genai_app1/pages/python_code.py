from openai import OpenAI
import streamlit as st


# Import OpenAI API client
# Replace 'openai_client' with the actual library you use to interact with the OpenAI API
# Example: import openai_client

# Read API key from file
with open("keys/.openai_api_key.txt", "r") as f:
    OPENAI_API_KEY = f.read().strip()

client = OpenAI(api_key=OPENAI_API_KEY)




# Streamlit UI

st.title("GenAI App - AI Code Reviewer")
    # user input 
st.header('Enter your python code')
prompt = st.text_area("Paste your Python code here:", height=200)
    
    # Button to trigger code review 
if st.button("Review the Code"):
    st.markdown("<h2 style='color:blue;'>Review Result</h2>", unsafe_allow_html=True)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Review the given python code and Generate what are the list of mistakes in the code and give fixed code by correcting the code"},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500
    )
    
    # Display the generated text
    generated_text = response.choices[0].message.content
    st.write(generated_text)
     
