# Vertex AI Studio: Generative AI Exploration & Prompt Engineering

![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
![Vertex AI](https://img.shields.io/badge/Vertex_AI-00L?style=for-the-badge&logo=google-cloud&logoColor=white&color=06162d)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

This repository contains the implementation and experimental results of the **Generative AI Studio** laboratory within Google Cloud's **Vertex AI** platform. The project focuses on leveraging Large Language Models (LLMs) for natural language tasks through advanced prompt design and parameter tuning.

### 🎯 Project Goal
The primary goal was to explore and master the Generative AI Studio interface to design, test, and export high-performing prompts for enterprise-level NLP tasks like summarization, extraction, and sentiment analysis.

### 💡 Key Skills Demonstrated

* **Prompt Engineering Architecture:** Developed both **Freeform** and **Structured** prompts, implementing **Zero-shot** and **Few-shot** learning techniques to guide model behavior.
* **Hyperparameter Tuning:** Optimized model outputs by strategically adjusting **Temperature**, **Top-K**, and **Top-P** settings to balance creativity and deterministic precision.
* **Response Validation:** Analyzed and iterated on LLM outputs to reduce hallucination and ensure factual consistency in text summarization.
* **SDK Integration:** Successfully exported visual experiments into production-ready **Python** code using the `google-cloud-aiplatform` library.

### 📂 Files Info:

* **src/main.py** — Python implementation of the optimized prompt logic using the Vertex AI SDK.
* **terraform/main.tf** — Infrastructure-as-Code snippet to enable necessary AI services within GCP.
* **.github/workflows/python-app.yml** — Automated CI/CD pipeline to validate code syntax and dependencies.
* **requirements.txt** — List of necessary Python libraries for local or cloud deployment.

### 🛠️ Technical Insights
During this lab, I explored how different sampling methods (Top-P vs. Top-K) affect the probability distribution of tokens, which is crucial for building reliable AI agents that require specific output formats (like JSON or Bullet Points).

---
*Created as part of my journey to become a Cloud AI Engineer.*
