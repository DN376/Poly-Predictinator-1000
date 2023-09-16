#this currently uses streamlit as the UI / "Frontend"
import streamlit as st
from gnews import GNews
import datetime
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')


def main():

    st.set_page_config(page_title="Quick Report",
                       page_icon=":rolled_up_newspaper:")
    st.header("Quick Report :rolled_up_newspaper:")

    subject = st.text_input('**Choose a Subject to Summarize:**')

    st.write("Subject: " + subject)

    with st.spinner("Removing Stopwords..."):
        cleanSubj = removeStops(subject)
    st.write("clean = " + cleanSubj)
    with st.spinner("Getting articles..."):
        google_news = GNews()
        news = google_news.get_news(cleanSubj)
    st.write("Found " + str(len(news)) + " articles")
    news1 = [news[0]]
    for article in news1:
        article_text = google_news.get_full_article(article['url']).text
        st.write(article_text)

def removeStops(subject):
    cachedStopWords = stopwords.words("english")
    return ' '.join([word for word in subject.split() if word not in cachedStopWords])

main()