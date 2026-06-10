<div align="center">

# 🎬 IMDb Movie Sentiment Analyzer

### *A production-ready NLP pipeline fine-tuning DistilBERT for real-time movie review sentiment classification.*

[![GitHub last commit](https://img.shields.io/github/last-commit/mohdali-dev/imdb-sentiment-analyzer?style=flat-square)](https://github.com/mohdali-dev/imdb-sentiment-analyzer/commits/main)
[![GitHub stars](https://img.shields.io/github/stars/mohdali-dev/imdb-sentiment-analyzer?style=flat-square&color=yellow)](https://github.com/mohdali-dev/imdb-sentiment-analyzer/stargazers)
[![Python Version](https://img.shields.io/badge/Python-3.9%20%7C%203.10-blue?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mohdali-dev/imdb-sentiment-analyzer/blob/main/notebooks/fine_tune_distilbert.ipynb)

[🤗 Model](https://huggingface.co/mohdali1/distilbert-imdb-sentiment) • [🚀 Live Demo](https://huggingface.co/spaces/mohdali1/imdb-sentiment-demo) • [📊 Dataset](https://huggingface.co/datasets/imdb)

</div>

---

## 📖 Overview

The **IMDb Movie Sentiment Analyzer** is an end-to-end Machine Learning project that demonstrates the complete lifecycle of building a Natural Language Processing (NLP) application. By fine-tuning a **DistilBERT** transformer model on the renowned **IMDb movie review dataset**, this project achieves high-accuracy binary sentiment classification (Positive vs. Negative).

Whether you are an NLP enthusiast, a recruiter reviewing my portfolio, or a developer wanting to integrate sentiment analysis, this repository provides a clean, reproducible, and production-oriented codebase.

## ✨ Key Features

- 🎯 **High Performance**: Achieved **90.92% validation accuracy** on a held-out test set.
- ⚡ **Optimized Inference**: Leveraging `distilbert-base-uncased` ensures 60% faster inference compared to standard BERT, with minimal accuracy drop.
- 🌐 **Interactive Web UI**: A fully functional, real-time Gradio demo hosted on Hugging Face Spaces.
- 📓 **Reproducible Pipeline**: A comprehensive Jupyter Notebook covering data loading, tokenization, training, evaluation, and model pushing to the Hub.
- 🤗 **Hub Integration**: Pre-trained weights and tokenizer are publicly available on the Hugging Face Model Hub.

## 🚀 Live Demo

Experience the model in action! Type or paste any movie review, and the model will predict its sentiment in real-time.

👉 **[Launch the IMDb Sentiment Analyzer Demo](https://huggingface.co/spaces/mohdali1/imdb-sentiment-demo)**

[![Gradio Demo](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue?style=for-the-badge)](https://huggingface.co/spaces/mohdali1/imdb-sentiment-demo)

## 📊 Model Performance & Metrics

The model was trained on 25,000 labeled IMDb reviews and evaluated on a separate validation split.

| Metric | Value |
| :--- | :--- |
| **Base Model** | `distilbert-base-uncased` |
| **Validation Accuracy** | **90.92%** |
| **Training Hardware** | Google Colab (Tesla T4 GPU) |
| **Training Time** | ~18 minutes |

### Confusion Matrix

| | Predicted Negative | Predicted Positive |
| :--- | :---: | :---: |
| **Actual Negative** | 2,280 (TN) | 220 (FP) |
| **Actual Positive** | 234 (FN) | 2,266 (TP) |

## 🛠️ Tech Stack

- **Language**: Python 3.9+
- **Deep Learning Framework**: PyTorch
- **NLP Library**: Hugging Face `transformers`, `datasets`
- **Model Architecture**: DistilBERT (Transformer-based)
- **UI / Deployment**: Gradio
- **Development Environment**: Google Colab, Jupyter Notebook

## 🗂️ Repository Structure

```text
imdb-sentiment-analyzer/
├── notebooks/                  # Jupyter notebook with the full training pipeline
│   └── fine_tune_distilbert.ipynb
├── requirements.txt            # Python dependencies for exact reproduction
├── .gitignore                  # Configured for Python, Jupyter, and OS files
├── LICENSE                     # MIT License
└── README.md                   # Project documentation
```

## ⚡ Getting Started

Follow these steps to set up the project locally and run the training pipeline.

### 1. Clone the Repository
```bash
git clone https://github.com/mohdali-dev/imdb-sentiment-analyzer.git
cd imdb-sentiment-analyzer
```

### 2. Set Up a Virtual Environment
It is highly recommended to use a virtual environment to manage dependencies.
```bash
# Create the environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the Training Pipeline
Launch Jupyter Notebook or JupyterLab and open the training file.
```bash
jupyter notebook
# Navigate to notebooks/fine_tune_distilbert.ipynb
```

## 🤗 Using the Pre-trained Model

You can easily integrate this model into your own Python applications using the Hugging Face `pipeline` API.

### Installation
```bash
pip install transformers torch
```

### Inference Code
```python
from transformers import pipeline

# Load the fine-tuned sentiment analysis pipeline
classifier = pipeline("sentiment-analysis", model="mohdali1/distilbert-imdb-sentiment")

# Test with sample reviews
reviews = [
    "This movie was absolutely fantastic! The acting was superb.",
    "A complete waste of time. The plot was boring and predictable."
]

results = classifier(reviews)
for review, result in zip(reviews, results):
    print(f"Review: {review}\nSentiment: {result['label']} (Confidence: {result['score']:.4f})\n")
```

## 🗺️ Roadmap

- [x] Fine-tune DistilBERT on IMDb dataset
- [x] Build and deploy Gradio interface on Hugging Face Spaces
- [ ] Add batch processing capabilities (CSV/JSON file uploads)
- [ ] Deploy backend API using FastAPI and Docker
- [ ] Experiment with larger models (RoBERTa, DeBERTa) for comparison

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! 
Feel free to check the [issues page](https://github.com/mohdali-dev/imdb-sentiment-analyzer/issues) or submit a Pull Request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

## 📫 Let's Connect!

If you found this project interesting or useful, feel free to reach out or check out my other work!

<div align="center">

**Muhammad Ali**  
*Aspiring AI/ML Engineer & Software Developer*

[![Portfolio](https://img.shields.io/badge/Portfolio-mohdali.me-black?style=for-the-badge&logo=firefox)](https://www.mohdali.me/)
[![GitHub](https://img.shields.io/badge/GitHub-mohdali--dev-black?style=for-the-badge&logo=github)](https://github.com/mohdali-dev)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Muhammad_Ali-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/mohdali1/)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-mohdali1-yellow?style=for-the-badge)](https://huggingface.co/mohdali1)
[![Email](https://img.shields.io/badge/Email-alisundusi10@gmail.com-red?style=for-the-badge&logo=gmail)](mailto:alisundusi10@gmail.com)

</div>

---
<div align="center">
  <sub>Built with ❤️ by <a href="https://github.com/mohdali-dev">Muhammad Ali</a></sub>
</div>
