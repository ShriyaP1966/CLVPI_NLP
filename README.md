# 🌍 Multilingual LLM Safety Evaluation Framework

A modular research framework for benchmarking, evaluating, and analyzing the safety of multilingual Large Language Models (LLMs). The framework is designed to compare model behavior across multiple languages and will later include an AI-powered safety classifier for unseen LLM responses.

---

## 🎯 Objectives

- Benchmark multilingual LLM safety performance
- Compare GPT and Gemini across English, Hindi, and Marathi
- Generate reproducible experiments
- Produce statistics and visualizations
- Build a reusable evaluation framework
- Extend the framework with an automated safety classifier

---

## ✨ Features

### ✅ Implemented

- Dataset validation
- UTF-8 sanitization
- Multilingual dataset loader
- Benchmark execution engine
- Provider Factory architecture
- Mock provider for testing
- Experiment management
- Result writer
- Configuration-driven execution

### 🚧 In Progress

- OpenAI integration
- Gemini integration
- Automatic response evaluation
- Statistics generation
- Graph generation
- Research report generation

### 🔮 Planned

- Multilingual safety classifier
- Additional LLM providers
- Interactive dashboard
- Web application

---

## 🌐 Languages

- 🇺🇸 English
- 🇮🇳 Hindi
- 🇮🇳 Marathi

---

## 📊 Benchmark Dataset

Current dataset includes:

- **104 multilingual prompt sets**
- **312 benchmark tasks**
- **13 attack categories**
- **3 languages**

---

## 🏗 Architecture

```text
Dataset
   │
   ▼
Validation
   │
   ▼
Task Generation
   │
   ▼
Provider Factory
   │
   ├── Mock
   ├── OpenAI
   └── Gemini
   │
   ▼
Benchmark Engine
   │
   ▼
Result Writer
   │
   ▼
Evaluation
   │
   ▼
Statistics & Visualizations
```

---

## 🛠 Tech Stack

**Language**
- Python 3.13

**Libraries**
- pandas
- numpy
- OpenAI API
- Google Gemini API
- matplotlib
- python-dotenv

**Translation**
- Hugging Face Transformers
- IndicTrans2

**Tools**
- Git
- GitHub
- VS Code

---

## 📂 Project Structure

```
NLP_Safety_Benchmark/
│
├── config/
├── data/
├── experiments/
├── outputs/
├── scripts/
│   ├── providers/
│   ├── analysis/
│   ├── dataset_loader.py
│   ├── result_writer.py
│   ├── run_experiment.py
│   ├── sanitize_dataset.py
│   ├── validate_dataset.py
│   └── utils.py
│
└── README.md
```

---

## 🚀 Getting Started

Clone the repository

```bash
git clone https://github.com/ShriyaP1966/CLVPI_NLP.git
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the benchmark

```bash
python scripts/run_experiment.py
```

---

## 🗺 Roadmap

- [x] Project foundation
- [x] Dataset validation
- [x] Benchmark execution engine
- [x] Provider Factory architecture
- [x] Mock provider
- [ ] OpenAI integration
- [ ] Gemini integration
- [ ] Automatic evaluation
- [ ] Statistics & graphs
- [ ] Research-ready reports
- [ ] Safety classifier
- [ ] Web interface

---

## 🎓 Research Vision

This project aims to evolve into a complete multilingual LLM safety evaluation platform by combining:

- Benchmarking
- Automated evaluation
- Statistical analysis
- Cross-model comparison
- AI-powered safety classification

The framework is designed to be modular, reproducible, and easily extendable for future LLMs and multilingual safety research.

---

## 📄 License

**All Rights Reserved.**

This repository is provided for viewing, educational, and research reference only.

No permission is granted to copy, modify, redistribute, or commercially use the source code without prior written permission from the author.

See the [LICENSE](LICENSE) file for full terms.

---

## 👩‍💻 Author

**Shriya Patil**

B.Sc. Artificial Intelligence

**Research Interests**
- Artificial Intelligence
- Large Language Models (LLMs)
- AI Safety
- Natural Language Processing
- Multilingual AI
