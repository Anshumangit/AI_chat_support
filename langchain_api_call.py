import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load your local variables securely from your untracked .env file
load_dotenv(override=True)

# Define your prompt variable

groq_openai_model="openai/gpt-oss-120b"
groq_url="https://api.groq.com/openai/v1"


# Point LangChain to Groq instead of OpenAI
llm = ChatOpenAI(
    base_url=groq_url,       # Routes requests to Groq
    api_key=os.getenv("GROQ_OPENAI_KEY"),            # Uses your free Groq key
    model=groq_openai_model                    # Swaps out GPT for a free model
)

tell_a_joke = "Tell me a short joke about a programmer."

# Invoke the execution
response = llm.invoke(tell_a_joke)

# Display result
print(response.content)
