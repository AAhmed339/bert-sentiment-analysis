

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
