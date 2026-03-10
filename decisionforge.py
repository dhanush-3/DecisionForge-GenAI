import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_groq_llm(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional business decision advisor."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama3-8b-8192"
        )

        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"Error occurred: {str(e)}"


def generate_decision(problem):

    prompt = f"""
You are a helpful business advisor.

Problem:
{problem}

Provide:
1. Three practical strategies
2. One risk for each strategy
3. One recommended approach

Be clear and practical.
"""

    return ask_groq_llm(prompt)


if __name__ == "__main__":
    problem = input("Enter your decision problem: ")

    print("\nGenerating complete decision analysis...\n")

    result = generate_decision(problem)

    print("\n=== DECISION ANALYSIS ===\n")
    print(result)