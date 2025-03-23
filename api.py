from fastapi import FastAPI
from utils import extract_news, analyze_sentiment, compare_sentiments, text_to_speech

app = FastAPI()

@app.get('/analyze/{company_name}')
def analyze(company_name: str):
    articles = extract_news(company_name)
    if not articles:
        return {'error': 'No articles found'}

    sentiments, topics = analyze_sentiment(articles)
    comparison = compare_sentiments(sentiments)
    speech_file = text_to_speech(comparison)

    return {
        'sentiment_report': sentiments,
        'topics': topics,
        'comparison': comparison,
        'audio_url': speech_file
    }
