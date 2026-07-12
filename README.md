# 🛡️ Multilingual LLM Safety Benchmark

> A research-oriented framework for evaluating the multilingual safety behaviour of Large Language Models (LLMs) against adversarial prompt attacks in **English, Hindi, and Marathi**.

---

## 📖 Overview

Large Language Models (LLMs) are increasingly deployed in real-world applications where safe and reliable responses are essential. However, most existing safety evaluations focus primarily on English, leaving multilingual safety behaviour underexplored.

This project aims to build a **reproducible multilingual benchmarking framework** for evaluating and comparing the safety behaviour of different LLMs across English, Hindi, and Marathi using adversarial prompts.

The benchmark is being developed as a research project with the goal of producing a publication-quality evaluation framework.

---

## 🎯 Objectives

- Build a multilingual safety benchmark for LLMs.
- Compare safety behaviour across multiple languages.
- Evaluate OpenAI GPT and Google Gemini models.
- Create a reproducible benchmarking pipeline.
- Generate structured outputs for research and analysis.

---

## 🌍 Languages

- 🇬🇧 English
- 🇮🇳 Hindi
- 🇮🇳 Marathi

---

## 🤖 Target Models

### Current
- Mock Provider (Pipeline Testing)

### Planned
- GPT-5 mini (OpenAI API)
- Gemini 2.5 Flash (Google AI API)

---

## 📊 Benchmark Dataset

| Attribute | Value |
|-----------|------:|
| Languages | 3 |
| Dataset Rows | 104 |
| Benchmark Tasks | 312 |
| Attack Categories | 13 |
| Prompt Variations | 8 |

---

## 🔄 Current Benchmark Pipeline

```text
Master Dataset
      │
      ▼
IndicTrans2 Translation
      │
      ▼
Manual Verification
      │
      ▼
UTF-8 Sanitization
      │
      ▼
Dataset Validation
      │
      ▼
Dataset Loader
      │
      ▼
312 Benchmark Tasks
      │
      ▼
Mock Provider
      │
      ▼
Response Collection
      │
      ▼
CSV Result Writer
```

---

## ⚙️ Features Implemented

### Dataset Processing
- ✅ UTF-8 dataset sanitization
- ✅ Dataset validation
- ✅ Required column validation
- ✅ Duplicate prompt detection
- ✅ Missing value detection

### Benchmark Engine
- ✅ Dataset loader
- ✅ Benchmark task generation
- ✅ Mock provider execution
- ✅ Result writer
- ✅ CSV result generation
- ✅ Execution summary
- ✅ Experiment metadata generation

---

## 🏗️ Project Structure

```text
CLVPI_NLP
│
├── config/
├── data/
├── dev_tools/
├── experiments/
├── logs/
├── outputs/
│   ├── raw/
│   ├── evaluated/
│   ├── merged/
│   ├── statistics/
│   └── figures/
│
├── scripts/
│   ├── analysis/
│   ├── providers/
│   ├── dataset_loader.py
│   ├── result_writer.py
│   ├── run_experiment.py
│   ├── sanitize_dataset.py
│   ├── validate_dataset.py
│   └── utils.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🛠️ Technology Stack

### Programming
- Python

### Data Processing
- Pandas

### Translation
- Hugging Face
- IndicTrans2

### APIs (Planned)
- OpenAI API
- Google Gemini API

### Version Control
- Git
- GitHub

---

## 🚀 Development Progress

### ✅ Completed
- [x] Project architecture
- [x] Configuration management
- [x] UTF-8 sanitization
- [x] Dataset validation
- [x] Dataset loader
- [x] Benchmark task generation
- [x] Mock execution engine
- [x] Result writer
- [x] CSV output generation
- [x] Execution summary

### 🚧 In Progress
- [ ] Provider Factory

### 📌 Planned
- [ ] OpenAI Provider
- [ ] Gemini Provider
- [ ] Automatic Evaluation Engine
- [ ] Statistical Analysis
- [ ] Graph Generation
- [ ] Cross-model Comparison
- [ ] Research Paper

---

## 📅 Development Timeline

| Day | Milestone | Status |
|------|-----------|--------|
| Day 1 | Project Foundation | ✅ |
| Day 2 | Benchmark Execution Engine | ✅ |
| Day 3 | Provider Factory | ⏳ |
| Day 4 | OpenAI Integration | ⏳ |
| Day 5 | Gemini Integration | ⏳ |
| Day 6 | Evaluation Engine | ⏳ |
| Day 7 | Statistics & Analysis | ⏳ |
| Day 8+ | Research & Documentation | ⏳ |

---

## 🔬 Research Focus

This benchmark investigates:

- Multilingual safety alignment
- Prompt injection robustness
- Jailbreak resistance
- Cross-language response consistency
- Safety behaviour across adversarial prompt attacks

---

## 👩‍💻 Author

**Shriya Patil**

B.Sc. Artificial Intelligence

Research Project • 2026

---

⭐ **Project Status:** Active Development
