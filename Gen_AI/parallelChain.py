import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

prompt1 = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant."),
        ("human", "Help me to find (i)Top Tourist Places based on this {city}")
    ]
)
model1 = ChatOpenAI(
    model = "gpt-5.5",
    api_key = os.getenv("OPENAI_API_KEY")
)
parser1 = StrOutputParser()

prompt2 = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant."),
        ("human", "Help me to find (ii)Top Food Places based on this {city}")
    ]
)
model2 = ChatOpenAI(
    model = "gpt-5.5",
    api_key = os.getenv("OPENAI_API_KEY")
)
parser2 = StrOutputParser()

prompt3 = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant."),
        ("human", "Help me to find (ii)Best time to visit based on this {city}")
    ]
)
model3 = ChatOpenAI(
    model = "gpt-5.5",
    api_key = os.getenv("OPENAI_API_KEY")
)
parser3 = StrOutputParser()


parallel_chain = RunnableParallel(
    chain1 = prompt1 | model1 | parser1,
    chain2 = prompt2 | model2 | parser2,
    chain3 = prompt3 | model3 | parser3
)

result = parallel_chain.invoke(
    {"city" : "Haridwar"}
)

print("========== Tourist Places ==========\n")
print(result["chain1"])

print("\n========== Food Places ==========\n")
print(result["chain2"])

print("\n========== Best Time ==========\n")
print(result["chain3"])