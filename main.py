import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found")

client = genai.Client(api_key=api_key)

while True:
    question=input("You: ")

    if question.lower() in ["exit", "quit"]:
        print("Gemini: Goodbye!")
        break

    response=client.models.generate_content(
        model="gemini-3.6-flash",
        contents=question
        )
    print("Gemini:",response.text) 