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
    google_news = GNews()

    subject = st.text_input('**Choose a Subject to Summarize:**')

    st.write("Subject: " + subject)

    cleanSubj = removeStops(subject)

    st.write("Subject: " + cleanSubj)# for debugging purposes ONLY

    news = getArticles(cleanSubj, google_news)

    st.write("Found " + str(len(news)) + " articles")
    
    newsSelection = presentOptions(news)

    displayText(newsSelection, google_news)

def removeStops(subject):
    with st.spinner("Removing Stopwords..."):
        cachedStopWords = stopwords.words("english")
        return ' '.join([word for word in subject.split() if word not in cachedStopWords])

def getArticles(cleanSubj, google_news):
    with st.spinner("Getting articles..."):
        news = google_news.get_news(cleanSubj)
    return news

def presentOptions(news):
    if(st.button("Main Article")):
        newsSelection = [news[0]]
    if(st.button("Top 5 Articles")):
        newsSelection = news[0:5]
    if(st.button("Top 10 Articles")):
        newsSelection = news[0:10]
    if(st.button("Top 25 Articles")):
        newsSelection = news[0:25]
    if(st.button("All Articles")):
        newsSelection = news
    return newsSelection

def displayText(newsSelection, google_news):
    for article in newsSelection:
        article_text = google_news.get_full_article(article['url']).title
        st.write(article_text)
        st.write("------\n")

main()