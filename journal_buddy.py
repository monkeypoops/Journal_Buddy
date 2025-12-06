import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPEN_API_KEY")

if not api_key:
    raise RuntimeError(
        "OPENAI_API_KEY not found. "
        "Create a .env file and add OPENAI_API_KEY=your_api_key_here"
    )

client = OpenAI(api_key=api_key)

def journal_prompt(name, mood, quote, minutes_per_day):
    """Turn user answers into a single prompt string."""
    prompt = f"""
You are an empathetic, encouraging called Journal Buddy.

Create a simple, safe daily journal for this person:

Name: {name}
Mood: {mood}
Inspirational quote: {quote}
Minutes per day: {minutes_per_day}

Requirements:
-
-
-
-
- Speak directly to {name} in an empathetic voice
"""
    return prompt.strip()

def get_journal_plan(prompt: str) -> str:
    """
    Call OpenAI's Responses API with a simple text prompt.
    
    We use response.output_text for convenience so students don't have to dig through the whole JSON.
    """
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
    )

    return response.output_text

def main():
    print("=" * 50)
    print("Welcome to Journal Buddy")
    print("=" * 50)

    name = input("What is your name? ")
    mood = input("How is your mood today? ")
    quote = input("Do you want an inspirational quote today? ")
    minutes_per_day = input("How many minutes do you want to write today? ")

    print("\nGreat {name}! I'm so excited to see what you will share tonight!\n")

    prompt = journal_prompt(name, mood, quote, minutes_per_day)
    