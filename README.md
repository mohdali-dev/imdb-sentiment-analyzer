# 🎬 Movie Sentiment Analyzer

A production-ready sentiment analysis tool built by fine-tuning a **DistilBERT** transformer model on the **IMDb movie review dataset**. This project demonstrates the complete lifecycle of an ML model, from data preprocessing to a live, interactive web demo.

## 🌐 Live Demo

Try the model in real time: [**IMDb Sentiment Analyzer Demo**](https://huggingface.co/spaces/mohdali1/imdb-sentiment-demo)

[![Gradio Demo](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/mohdali1/imdb-sentiment-demo)

## 📊 Model Performance

- **Validation Accuracy**: **90.92%**
- **Base Model**: `distilbert-base-uncased`
- **Training Dataset**: 25,000 labeled IMDb reviews
- **Training Time**: ~18 minutes on Google Colab Tesla T4 GPU

|              | Predicted Negative | Predicted Positive |
|--------------|--------------------|--------------------|
| Actual Negative | 2,280              | 220                |
| Actual Positive | 234                | 2,266              |

## 🛠️ Tech Stack

- **Language**: Python 3.8+
- **Framework**: PyTorch, Hugging Face Transformers
- **Model**: DistilBERT
- **Interface**: Gradio
- **Environment**: Google Colab

## 🗂️ Repository Structure

```
imdb-sentiment-analyzer/
├── notebooks/             # Jupyter notebook with full training pipeline
│   └── fine_tune_distilbert.ipynb
├── requirements.txt       # Python dependencies for exact reproduction
├── .gitignore            # Properly configured for Python/Notebooks
├── LICENSE               # MIT License
└── README.md             # This file
```

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/mohdali-dev/imdb-sentiment-analyzer.git
   cd imdb-sentiment-analyzer
   ```

2. **Set up a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: `venv\Scripts\activate`
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Jupyter Notebook**
   Launch Jupyter and open `notebooks/fine_tune_distilbert.ipynb` to explore the end-to-end pipeline.

   ```bash
   jupyter notebook
   ```

## 🤗 Using the Model

You can load the model directly from Hugging Face Hub:

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="mohdali1/distilbert-imdb-sentiment")

result = classifier("This movie was absolutely fantastic!")
print(result)  # [{'label': 'POSITIVE', 'score': 0.99...}]
```

## 📫 Connect with Me

- **GitHub**: [mohdali-dev](https://github.com/mohdali-dev)
- **LinkedIn**: [Muhammad Ali](https://www.linkedin.com/in/mohdali1/)
- **Hugging Face**: [mohdali1](https://huggingface.co/mohdali1)

## 📝 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
