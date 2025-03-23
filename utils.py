import requests
from transformers import pipeline
from gtts import gTTS
import os


sentiment_analyzer = pipeline('sentiment-analysis', model='distilbert-base-uncased', device=0)  # Uses GPU if available

def extract_news(company_name):
    url = f'https://newsapi.org/v2/everything?q={company_name}&apiKey=YOUR_API_KEY'
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        return [{'title': article['title'], 'content': article['content']} for article in articles]
    return []


def analyze_sentiment(articles):
    sentiments = []

    for article in articles:
        if article['content']:
            result = sentiment_analyzer(article['content'])[0]
            sentiments.append({'title': article['title'], 'sentiment': result['label'], 'score': result['score']})
    return sentiments


def compare_sentiments(sentiments):
    positive_count = len([article for article in sentiments if article['sentiment'] == 'POSITIVE'])
    negative_count = len([article for article in sentiments if article['sentiment'] == 'NEGATIVE'])
    neutral_count = len([article for article in sentiments if article['sentiment'] == 'NEUTRAL'])

    comparison = f"Positive articles: {positive_count}; Negative articles: {negative_count}; Neutral articles: {neutral_count}"
    return comparison


def text_to_speech(text):
    tts = gTTS(text=text, lang='hi')
    audio_file = 'speech_output.mp3'
    tts.save(audio_file)
    return audio_file
