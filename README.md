TO FIX PIP ERROR

Step 1: Clean out the broken fileIn your Administrator Command Prompt, run this command to delete the broken web page file:

bash
del get-pip.py

Step 2: Download the file manually using your Web BrowserOpen your internet browser (Chrome, Edge, Firefox, etc.).Click this link or paste it into your browser address bar: https://bootstrap.pypa.io/get-pip.py.Note: If a wall of code appears on your screen, right-click anywhere on the page and select Save As....Save the file to your standard Downloads folder. Make sure the name is exactly get-pip.py.

Step 3: Run the installer from your Downloads folderNow go back to your Administrator Command Prompt and run these commands to navigate to your downloads folder and execute the real script:Move into your downloads folder:

bash
cd %USERPROFILE%\Downloads

Run the actual script using the Python launcher:

bash
py get-pip.py

Step 4: Verify the installationOnce the installation text stops moving, test it by checking the version:

bash
py -m pip --version

==================================================================

NOTE: The Alternative "No-File" Solution (For the future)

If pip ever breaks again in the future and you want to fix it without downloading any files into your project folders, use the built-in Python bootstrap engine. This uses your computer's internal memory to pull files instead of creating a physical file in your workspace:

bash
py -m ensurepip --default-pip

=====================================================================

sample code

import os
import openai

# 1. Initialize Client 1 (Dedicated for Llama models)

client_llama = openai.OpenAI(
base_url="https://api.groq.com/openai/v1",
api_key=os.environ.get("GROQ_API_KEY_ONE") # Key assigned for Llama tasks
)

# 2. Initialize Client 2 (Dedicated for OpenAI / Reasoning models)

client_reasoning = openai.OpenAI(
base_url="https://api.groq.com/openai/v1",
api_key=os.environ.get("GROQ_API_KEY_TWO") # Key assigned for Advanced tasks
)

# =====================================================================

# HOW TO RUN CALLS INDEPENDENTLY

# =====================================================================

# Call the Llama 4 Scout model using Client 1

llama_response = client_llama.chat.completions.create(
model="meta-llama/llama-4-scout-17b-16e-instruct", # Latest active production Llama 4
messages=[{"role": "user", "content": "Hello from Llama!"}]
)
print("Llama Output:", llama_response.choices[0].message.content)

# Call the GPT-OSS 120B model using Client 2

reasoning_response = client_reasoning.chat.completions.create(
model="openai/gpt-oss-120b", # Hidden advanced model string
messages=[{"role": "user", "content": "Hello from Advanced Reasoning!"}]
)
print("Reasoning Output:", reasoning_response.choices[0].message.content)

===================================================================================

IGONORE .env

The M symbol you see next to your .env file stands for Modified. This means Git is actively tracking your .env file, and if you push your code, your secret API keys will be exposed publicly on GitHub.

To fix this immediately and securely remove .env from Git without deleting your actual file, follow these steps:

Step 1: Tell Git to Ignore the FileOpen your terminal inside your project directory and run this exact command to remove the .env file from Git's tracking memory

:bash

git rm --cached .env

(Note: The --cached flag is critical because it tells Git to stop tracking the file while safely keeping the actual .env file intact on your local computer [1].)

Step 2: Add it to .gitignoreOpen or create a file named .gitignore in your project's root folder and add .env to it so Git never tracks it again:text# Ignore local environment variables
.env

Step 3: Commit and Push the FixNow, save these changes and push them to GitHub. The M symbol will disappear, and your keys will remain safe locally

:bash

git add .gitignore

git commit -m "chore: remove/stop tracking .env from git tracking and add to gitignore"

git push origin main

Best Practice: Create a Template FileSince other developers (or your future self) will need to know what API keys your script expects without seeing the actual secret values, create a dummy template file named .env.example:text# .env.example (Safe to push to GitHub)
GROQ_API_KEY_ONE=your_llama_key_here
GROQ_API_KEY_TWO=your_openai_key_here

=======================================================

To install langchain
=> pip install langchain_openai

To install litle llm
=> pip install litellm python-dotenv

======================================================================================

# Connect to OpenAI client library

# A thin wrapper around calls to HTTP endpoints

openai = OpenAI()

# For Gemini, DeepSeek and Groq, we can use the OpenAI python client

# Because Google and DeepSeek have endpoints compatible with OpenAI

# And OpenAI allows you to change the base_url

anthropic_url = "https://api.anthropic.com/v1/"
gemini_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
deepseek_url = "https://api.deepseek.com"
groq_url = "https://api.groq.com/openai/v1"
grok_url = "https://api.x.ai/v1"
openrouter_url = "https://openrouter.ai/api/v1"
ollama_url = "http://localhost:11434/v1"

anthropic = OpenAI(api_key=anthropic_api_key, base_url=anthropic_url)
gemini = OpenAI(api_key=google_api_key, base_url=gemini_url)
deepseek = OpenAI(api_key=deepseek_api_key, base_url=deepseek_url)
groq = OpenAI(api_key=groq_api_key, base_url=groq_url)
grok = OpenAI(api_key=grok_api_key, base_url=grok_url)
openrouter = OpenAI(base_url=openrouter_url, api_key=openrouter_api_key)
ollama = OpenAI(api_key="ollama", base_url=ollama_url)
