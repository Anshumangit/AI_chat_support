import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

gemini_api_key = os.getenv("GEMINI_API_KEY")
groq_llama_key = os.getenv("GROQ_LLAMA_KEY")
groq_openai_key = os.getenv("GROQ_OPENAI_KEY")

# # Check the key

if gemini_api_key:
    print(f"Gemini api key exists and looks good so far: {gemini_api_key[:4]}")
else:
    print("Gemini api key does not exist")    

if groq_llama_key:
    print(f"Groq Llama api key exists and looks good so far: {groq_llama_key[:7]}")
else:
    print("Groq Llama api key does not exist")    

if groq_openai_key:
    print(f"Groq OpenAI api key exists and looks good so far: {groq_openai_key[:6]}")
else:
    print("Groq OpenAI api key does not exist")    

gemini_url="https://generativelanguage.googleapis.com/v1beta/"
groq_url="https://api.groq.com/openai/v1"

gemini_model="gemini-3-flash-preview"
groq_llama_model="llama-3.3-70b-versatile" 
groq_openai_model="openai/gpt-oss-120b"

gemini=OpenAI(api_key=gemini_api_key, base_url=gemini_url)
groq_llama=OpenAI(api_key=groq_llama_key, base_url=groq_url)
groq_openai=OpenAI(api_key=groq_openai_key, base_url=groq_url)

message="Hello Gemini! Tell me about your self in a snarky way and keep it short"

messages=[
          {"role":"system","content":"You are a helpful assistant."},
          {"role":"user","content":message}
          ]

groq_llama_response=groq_llama.chat.completions.create(model=groq_llama_model, messages=messages)
groq_openai_response=groq_openai.chat.completions.create(model=groq_openai_model, messages=messages)

print("\n--- Fetching Responses ---")

try:
    gemini_response=gemini.chat.completions.create(model=gemini_model, messages=messages)
    print(f"Gemini Response: {gemini_response.choices[0].message.content}\n")
except Exception as e:
    print(f"Gemini response error: {e}\n")

try:
    print(f"Groq Llama Response: {groq_llama_response.choices[0].message.content}\n")
except Exception as e:
    print(f"Groq Llama response error: {e}\n")

try:
    print(f"Groq OpenAI Response: {groq_openai_response.choices[0].message.content}\n")
except Exception as e:
    print(f"Groq OpenAI response error: {e}\n")
