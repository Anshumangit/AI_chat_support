import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

API_KEY = os.getenv("GEMINI_API_KEY")

# # Check the key

if not API_KEY:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
elif not API_KEY.startswith("AIz"):
    print("An API key was found, but it doesn't start AIz; please check you're using the right key - see troubleshooting notebook")
elif API_KEY.strip() != API_KEY:
    print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
else:
    print("API key found and looks good so far!")

message="Hello Gemini! Can you tell me a joke about AI?"

messages=[
          {"role":"system","content":"You are a helpful assistant."},
          {"role":"user","content":message}
          ]

gemini=OpenAI(base_url="https://generativelanguage.googleapis.com/v1beta/", api_key=API_KEY)

response=gemini.chat.completions.create(model="gemini-3-flash-preview", messages=messages)

print(response.choices[0].message.content)

