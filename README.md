

# BERT Sentiment Analysis (Transformers)

This project demonstrates sentiment analysis using a pretrained BERT model
via HuggingFace Transformers.

## Model
- DistilBERT (fine-tuned on SST-2)
- Bidirectional Transformer
- Pretrained model (no heavy training required)

## What the model does
Given an input sentence, the model predicts:
- POSITIVE
- NEGATIVE

## Example
```python
sentiment("I really love this movie")
## How to Run

Install the required libraries:
```bash
pip install torch transformers
from transformers import pipeline

sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

sentiment("I really love this movie")
