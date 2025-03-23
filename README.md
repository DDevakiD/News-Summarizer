# News Summarization App

## Overview
The News Summarization App is a Python-based application that extracts news articles about a specified company, analyzes their sentiment, and provides a summarized sentiment comparison. Additionally, it supports converting summarized text to speech in Hindi.

## Features
- Fetch news articles about a specified company from NewsAPI.
- Perform sentiment analysis on the articles using Hugging Face Transformers (DistilBERT).
- Summarize sentiment statistics (Positive, Negative, Neutral).
- Convert summary text to speech using Google Text-to-Speech (gTTS).
- Supports GPU acceleration if available.

## Requirements
- Python 3.7+
- Install dependencies via:
```bash
pip install -r requirements.txt
```

### Dependencies
- `transformers`
- `torch`
- `gtts`
- `requests`
- `fastapi`
- `uvicorn`

## Installation
1. Clone the repository:
```bash
git clone https://github.com/your-username/news-summarization-app.git
```
2. Navigate to the project directory:
```bash
cd news-summarization-app
```
3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage
1. Run the FastAPI server:
```bash
uvicorn api:app --reload
```
2. Make requests to the API using tools like Postman or cURL.

## API Endpoints
- `/extract_news`: Fetches news articles based on a company name.
- `/analyze_sentiment`: Analyzes the sentiment of fetched news articles.
- `/compare_sentiments`: Provides a summary of positive, negative, and neutral articles.
- `/text_to_speech`: Converts the summary text to Hindi speech.

## Notes
- Make sure to replace `YOUR_API_KEY` in the `extract_news` function with your actual NewsAPI key.
- Ensure enough free disk space is available if using GPU.

## License
This project is licensed under the MIT License.

## Acknowledgements
- Hugging Face Transformers
- NewsAPI
- Google Text-to-Speech (gTTS)

