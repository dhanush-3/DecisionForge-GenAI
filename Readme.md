# 🤖 DecisionForge AI

### Strategic Decision Assistant powered by Generative AI

DecisionForge AI is an intelligent **decision-support system** that leverages **Large Language Models (LLMs)** and **structured strategic frameworks** to help users make informed decisions in complex scenarios.

The system analyzes user queries using established business and strategic models such as **SWOT Analysis**, **Porter’s Five Forces**, and **Risk-Based Strategy Evaluation**, providing structured insights and actionable recommendations.

---

# 📌 Features

* 🧠 **AI-Powered Decision Support**
  Uses LLMs to analyze real-world problems and generate strategic recommendations.

* 📊 **Structured Strategic Analysis**
  Automatically applies frameworks like:

  * SWOT Analysis
  * Porter’s Five Forces
  * Risk Evaluation

* ⚡ **Retrieval-Augmented Generation (RAG)**
  Retrieves relevant contextual knowledge before generating responses.

* 🔄 **Adaptive Strategy Recommendations**
  Generates multiple practical strategies with benefits, risks, and implementation suggestions.

* 💻 **Interactive Web Interface**
  Built with Streamlit for a simple and user-friendly experience.

---

# 🏗️ System Architecture

```
User
 │
 ▼
Streamlit Frontend
 │
 ▼
Python Backend
 │
 ▼
Context Retrieval (RAG)
 │
 ▼
Vector Database
 │
 ▼
Large Language Model (LLM)
 │
 ▼
Structured Strategic Response
```

---

# ⚙️ Tech Stack

| Layer            | Technology            |
| ---------------- | --------------------- |
| Frontend         | Streamlit             |
| Backend          | Python                |
| AI Model         | LLaMA / Mixtral       |
| LLM API          | Groq                  |
| Retrieval System | RAG                   |
| Embeddings       | Sentence Transformers |
| Vector Storage   | FAISS / ChromaDB      |

---

# 🧠 Decision Frameworks Used

## SWOT Analysis

Evaluates internal and external factors affecting a decision.

* **Strengths**
* **Weaknesses**
* **Opportunities**
* **Threats**

---

## Porter’s Five Forces

Analyzes competitive environments.

* Threat of New Entrants
* Bargaining Power of Buyers
* Bargaining Power of Suppliers
* Threat of Substitutes
* Competitive Rivalry

---

## Risk-Based Strategy Planning

Each strategy includes:

* Goal
* Key Activities
* Expected Benefits
* Risk Level (1–10)

---

# 📂 Project Structure

```
DecisionForge-AI
│
├── app.py                # Streamlit frontend
├── rag.py                # Retrieval system
├── requirements.txt      # Dependencies
├── README.md
│
├── prompts/              # Prompt templates
├── vector_db/            # Vector database
├── utils/                # Helper functions
└── models/               # Local / API models
```

---

# 🚀 Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/decisionforge-ai.git
cd decisionforge-ai
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Add API Key

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

---

### 4️⃣ Run the Application

```
streamlit run app.py
```

---

# 💡 Example Use Case

### User Input

```
A startup wants to launch a new product with limited resources.
What strategy should they follow?
```

### AI Output

* SWOT Analysis
* Market Competitive Analysis
* Practical Strategies
* Risk Assessment
* Recommended Strategic Approach

---

# 🎯 Use Cases

* Startup strategy planning
* Business decision support
* Product launch analysis
* Strategic risk evaluation
* Educational learning tool for business frameworks

---

# 📈 Future Improvements

* Multi-agent decision analysis
* Real-time market data integration
* Visualization dashboards
* Multi-model LLM support
* SaaS deployment

---

# 👨‍💻 Author

**Dhanush Arrabolu**

Aspiring **AI Full Stack Developer** passionate about building intelligent systems using **Generative AI, backend development, and modern AI architectures**.

---

# ⭐ Support

If you find this project useful, consider giving it a **⭐ on GitHub** to support the project.
