import streamlit as st
import requests
from rag import retrieve_context


MODEL_NAME = "tinyllama"   # keep lightweight


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

    data = response.json()
    return data.get("response", "No response generated.")


def generate_decision(problem):

    context = retrieve_context(problem)

    prompt = f"""
Use the following business frameworks:
{context}

Now analyze:
{problem}

Generate structured decision analysis.
"""

    return ask_local_llm(prompt)


# -------- Streamlit UI --------

st.set_page_config(page_title="DecisionForge AI", layout="centered")

st.title("🧠 DecisionForge - Generative AI System")
st.write("Enter your problem and get AI-powered structured decision analysis.")

user_input = st.text_area("Enter your decision problem:")

if st.button("Generate Decision"):
    if user_input.strip() != "":
        with st.spinner("Generating analysis..."):
            result = generate_decision(user_input)
        st.success("Analysis Generated!")
        st.markdown("### 📊 Decision Report")
        st.write(result)
    else:
        st.warning("Please enter a problem.")