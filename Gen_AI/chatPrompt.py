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
    api_key = os.getenv("ANTHROPIC_API_KEY")
)

# Step 3: Create Parser
parser = StrOutputParser()

# Step 4: Invoke Prompt
prompt_value = chat_prompt.invoke(
    {
        "topic": "Cricket"
    }
)

print("----- Prompt Output -----")
print(prompt_value)

# Step 5: Invoke Model
response = model.invoke(prompt_value)

print("\n----- Model Output -----")
print(response)

# Step 6: Invoke Parser
final_output = parser.invoke(response)

print("\n----- Final Output -----")
print(final_output)