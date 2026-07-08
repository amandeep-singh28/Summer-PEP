import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant and an expert joke generator."),
        ("human", "Generate {no_of_jokes} jokes on the topic '{topic}'.")
    ]
)

prompt2 = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant and an expert joke generator."),
        (
            "human", "Analyze the following joke(s):{response}Create a better and funnier version.Return the response in the following format:"
            "Old Joke:"
            "Analysis:"
            "New Joke:")
    ]
)

model = ChatOpenAI(
    model = "gpt-5.5",
    api_key = os.getenv("OPENAI_API_KEY")
)

model2 = ChatAnthropic(
    model = "claude-sonnet-5",
    api_key = os.getenv("ANTHROPIC_API_KEY")
)

parser = StrOutputParser()

chain = prompt | model | parser

chain2 = prompt2 | model2 | parser

result = chain.invoke(
    {
        "topic" : "Dad Jokes",
        "no_of_jokes" : 10
    }
)


final_response = chain2.invoke(
    {
        "response": result
    }
)
print(final_response)

chain.get_graph().print_ascii()