import os
from litellm import completion
from dotenv import load_dotenv

load_dotenv(override=True)

# 1. Get the key safely from your .env file into a standard Python variable
gemini_api_key = os.getenv("GEMINI_API_KEY")


if gemini_api_key:
    print(f"Gemini api key exists and looks good so far: {gemini_api_key[:4]}")
else:
    print("Gemini api key does not exist") 

messages = [{"role": "user", "content": "Say hello!"}]

# 2. Hand the variable directly to LiteLLM using the 'api_key' parameter
response = completion(
    model="gemini/gemini-3-flash-preview", # LiteLLM requires the provider prefix (gemini/) to be explicitly included in the model string. 
    messages=messages,
    api_key=gemini_api_key # <--- LiteLLM will read this perfectly! or you can set it as an environment eg. os.getenv("GEMINI_API_KEY")
)

print(response.choices[0].message.content)
