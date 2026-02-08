from transformers import pipeline

def main():
    sentiment = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )

    tests = [
        "I really love this movie",
        "This film is terrible",
        "Amazing acting and story",
        "I will never watch this again"
    ]

    for text in tests:
        result = sentiment(text)[0]
        print(f"{text} -> {result['label']} ({result['score']:.4f})")

if __name__ == "__main__":
    main()
