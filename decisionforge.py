import requests

MODEL_NAME = "tinyllama"   # use smaller model


def ask_local_llm(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        },
        timeout=300
    )

    print("STATUS CODE:", response.status_code)
    print("RAW TEXT:", response.text)

    try:
        return response.json().get("response", "No response key found.")
    except Exception as e:
        return f"JSON error: {e}"


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

    return ask_local_llm(prompt)


if __name__ == "__main__":
    problem = input("Enter your decision problem: ")

    print("\nGenerating complete decision analysis...\n")

    result = generate_decision(problem)

    print("\n=== DECISION ANALYSIS ===\n")
    print(result)