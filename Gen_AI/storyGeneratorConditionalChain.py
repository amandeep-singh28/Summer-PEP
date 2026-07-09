import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableBranch

load_dotenv()

age = int(input("Enter age:"))
def func1(data):
    age = data["age"]

    if age < 18:
        return True
    return False


def func2(data):
    age = data["age"]

    if age >= 18:
        return True
    return False
    
kidStories_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant. Your work is to generate kids stories in a polite and respectful manner. Stories must be in a creative so that the kids can enjoy it."),
        ("human", "Generate 1 story. Format would be (i)Title (ii)Story (iii)Conclusion")
    ]
)
adultStories_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant. Your work is to generate horror stories. Stories must be in a creative so that the adults can enjoy it."),
        ("human", "Generate 1 story. Format would be (i)Title (ii)Story (iii)Conclusion")
    ]
)
model = ChatOpenAI(
    model = "gpt-5.5",
    api_key = os.getenv("OPENAI_API_KEY")
)

parser = StrOutputParser()

chain1 = kidStories_prompt | model | parser
chain2 = adultStories_prompt | model | parser

conditional_chain = RunnableBranch(
    (func1, chain1),
    (func2, chain2),
    chain2
)

result = conditional_chain.invoke(
    {
        "age" : age
    }
)

print(result)