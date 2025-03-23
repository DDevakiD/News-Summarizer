import streamlit as st 
import requests

st.title('News Summarization & Sentiment Analysis App')

# User Input
company_name = st.text_input('Enter Company Name')

if st.button('Analyze') and company_name:
    # Send request to FastAPI backend
    response = requests.get(f'http://127.0.0.1:8000/analyze/{company_name}')
    
    if response.status_code == 200:
        result = response.json()
        
        # Display Sentiment Analysis Report
        st.subheader('Sentiment Analysis Report')
        sentiment_report = result.get('sentiment_report', [])
        
        if sentiment_report:
            for article in sentiment_report:
                st.write(f"Title: {article['title']}")
                st.write(f"Sentiment: {article['sentiment']}")
                st.write(f"Score: {article['score']}")
                st.write("---")
        else:
            st.write("No sentiment analysis report found.")
        
        # Display Hindi Speech Output
        st.subheader('Hindi Speech Output')
        audio_url = result.get('audio_url')
        
        if audio_url:
            st.audio(audio_url)
        else:
            st.write('No audio generated.')
    else:
        st.write('Error fetching data from the backend. Make sure FastAPI is running.')
