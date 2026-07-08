import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
import streamlit as st
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

parser = StrOutputParser()

llm = ChatAnthropic(
    model="claude-sonnet-5",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

st.header("College Research Assistant")

info_type = st.selectbox(
    "What would you like to know?",
    [
        "Overview",
        "Admissions",
        "Courses",
        "Fees",
        "Placements",
        "Scholarships",
        "Campus Life"
    ]
)

college_name = st.text_input("Enter college name: ")

if st.button("Submit"):
    system_prompt = f"""
    You are a College Research Assistant.

    The user wants information about:
    {info_type}

    Generate exactly 5 concise points about the college '{college_name}'.
    Keep the tone polite and informative.
    """
    response = llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=f"Tell me about {college_name}.")
    ])
    result = parser.invoke(response)

    st.subheader(f"{info_type} of {college_name}")
    st.write(result)