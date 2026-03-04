# 🧠 DecisionForge - Multi-Agent Generative AI System

## 🚀 Overview
DecisionForge is a local Generative AI decision-making system built using LLMs, RAG, and multi-agent prompt orchestration. It runs fully offline using Ollama and TinyLlama.

## 🏗 Architecture
- Python Backend
- Ollama (Local LLM Server)
- TinyLlama (Transformer-based LLM)
- FAISS (Vector Database - ANN Search)
- Sentence Transformers (Embeddings)
- RAG (Retrieval Augmented Generation)
- Multi-Agent Prompt Simulation
- Streamlit Web UI

## 🧠 Features
- Role-based Prompt Engineering
- Multi-agent reasoning (Strategist, Risk Analyst, Architect)
- Semantic Retrieval using FAISS
- Structured Decision Output
- Fully Offline Deployment

## 🛠 Installation

```bash
pip install -r requirements.txt
ollama pull tinyllama
streamlit run app.py