# 🎓🔍 Chat With arXiv — *Your Local AI Research Buddy*

Welcome to **Chat With arXiv**, a lightweight, offline‑friendly research assistant powered by **Ollama**, **Agno**, and **Streamlit**.  
It’s like having a tiny PhD student living inside your computer… except it works faster, never complains, and doesn’t need coffee.

***

## ✨ What does it do?

This project lets you:

*   💬 **Ask natural questions**, like *"Find recent papers on multimodal models"*
*   🔎 **Search arXiv automatically** using built‑in tools
*   🧠 **Summarize papers**, compare topics, and explore research directions
*   🏃‍♂️ **Run fully locally** thanks to smaller models like **llama3.2:3b**
*   🪶 All with a lightweight footprint — no GPUs required (but welcome)!

***

## 🚀 How it works (in human language)

1.  You type a question into the Streamlit UI.
2.  **Agno Agent** receives it and decides:
    *   “Hmm, should I think… or should I call the arXiv tool?”
3.  If needed, it uses **ArxivTools** to fetch papers.
4.  Your local LLM (like `llama3.2:3b`) summarizes them for you.
5.  The assistant hands you results in beautiful markdown.
6.  You say “whoa, cool.”
7.  Repeat.

***

## 🧩 Tech Stack

*   **Python** — obviously.
*   **Streamlit** — clean UI with almost no effort.
*   **Agno** — agent framework that handles tools, context & reasoning.
*   **Ollama** — local model runner giving you LLM superpowers.
*   **llama3.2:3b** — tiny but mighty; supports tool calling and runs on potatoes.

***

## 📦 Installation

Clone the repo:

```bash
git clone https://github.com/your-username/chat-with-arxiv.git
cd chat-with-arxiv
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Make sure you have **Ollama** installed and pull your model:

```bash
ollama pull llama3.2:3b
```

Run the app:

```bash
streamlit run app.py
```

Boom. You’re live. 🎉

***

## 🧪 Example Queries

Try these inside the app:

*   *“Find me recent papers about AI agents.”*
*   *“Summaries of arXiv papers on graph neural networks.”*
*   *“What’s new in diffusion models?”*
*   *“Compare recent Llama vs Mistral research directions.”*

***