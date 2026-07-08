import os
from dotenv import load_dotenv
from anthropic import Anthropic
import streamlit as st

load_dotenv()

client = Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)
#Static Prompt for College Research Assistant
system_prompt = """
You are a College Research Assistant.

Your responsibilities are:
- Answer questions about colleges and universities.
- Provide information about admissions, courses, fees, placements, scholarships, rankings, and campus life.
- If the question is unrelated to colleges, politely respond:
  'I am a College Research Assistant and can only answer college-related queries.'
"""

st.set_page_config(
    page_title="College Research Assistant",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 College Research Assistant")

st.write("Ask any question related to colleges, admissions, fees, placements, scholarships, or rankings.")

#Asking for users query

user_query = st.text_input("Ask your college-related question: ")

if st.button("Get Answer"):

    if user_query.strip() == "":
        st.warning("Please enter a question.")

    else:

        with st.spinner("Searching..."):

            response = client.messages.create(
                model="claude-sonnet-5",   # Use the model available to your account
                max_tokens=2000,
                system=system_prompt,
                messages=[
                    {
                        "role": "user",
                        "content": user_query
                    }
                ]
            )

        st.success("Answer")

        st.write(response.content[0].text)