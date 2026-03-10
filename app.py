import os
import streamlit as st
from rag import retrieve_context
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def ask_groq_llm(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are DecisionForge AI, a professional strategic decision-making assistant."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            model="llama-3.1-8b-instant"
        )

        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"


def main():
    st.set_page_config(
        page_title="DecisionForge AI",
        page_icon="🤖",
        layout="wide"
    )

    # ---------- SIDEBAR ----------
    st.sidebar.title("⚙️ DecisionForge Settings")

    use_context = st.sidebar.checkbox("Enable RAG Context")

    if st.sidebar.button("Clear Chat"):
        st.session_state.messages = []

    st.sidebar.markdown("---")
    st.sidebar.markdown("### About")
    st.sidebar.write(
        "DecisionForge AI helps you make **strategic decisions** with structured advice."
    )

    # ---------- MAIN HEADER ----------
    st.title("🤖 DecisionForge AI")
    st.markdown("### Strategic Decision Assistant")

    # ---------- SESSION STATE ----------
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # ---------- DISPLAY CHAT ----------
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # ---------- USER INPUT ----------
    user_input = st.chat_input("Ask your decision question...")

    if user_input:

        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Analyzing decision..."):

                context = ""

                if use_context:
                    try:
                        context = retrieve_context(user_input)
                    except Exception as e:
                        st.warning(f"Context error: {e}")

                prompt = f"""
You are DecisionForge AI, a professional strategic decision-making assistant.

User Question:
{user_input}

Context:
{context}

Provide:
1. Three practical strategies
2. One risk for each strategy
3. One recommended approach

Be clear, structured, and practical.
"""

                answer = ask_groq_llm(prompt)

                st.markdown(answer)

        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )


if __name__ == "__main__":
    main()