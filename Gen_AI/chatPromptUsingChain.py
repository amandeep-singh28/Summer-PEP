from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

# Step 1: Create Prompt
chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful AI assistant."),
        ("human", "Explain {topic} in simple words.")
    ]
)

# Step 2: Create Model
model = ChatAnthropic(
    model="claude-sonnet-5",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

# Step 3: Create Parser
parser = StrOutputParser()

# Step 4: Create Chain
chain = chat_prompt | model | parser

# Step 5: Invoke the Chain
result = chain.invoke(
    {
        "topic": "Cricket"
    }
)

# Step 6: Print the Final Output
print(result)