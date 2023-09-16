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

    news = getArticles(cleanSubj, google_news)

    st.write("Found " + str(len(news)) + " articles")
    
    newsSelection = presentOptions(news, google_news)

    displayText(newsSelection, google_news)

def removeStops(subject):
    with st.spinner("Removing Stopwords..."):
        cachedStopWords = stopwords.words("english")
        return ' '.join([word for word in subject.split() if word not in cachedStopWords])

def getArticles(cleanSubj, google_news):
    with st.spinner("Getting articles..."):
        news = google_news.get_news(cleanSubj)
    return news

def presentOptions(news, google_news):
    if(st.button("Main Article")):
        newsSelection = getTopXArticles(1, news, google_news)
    if(st.button("Top 5 Articles")):
        newsSelection = getTopXArticles(5, news, google_news)
    if(st.button("Top 10 Articles")):
        newsSelection = getTopXArticles(10, news, google_news)
    if(st.button("Top 25 Articles")):
        newsSelection = getTopXArticles(25, news, google_news)
    if(st.button("Top 50 Articles")):
        newsSelection = getTopXArticles(50, news, google_news)
    return newsSelection

def getTopXArticles(x, news, google_news):
    newsSelection = []
    for article in news:
        full_article = google_news.get_full_article(article['url'])
        if full_article is not None:
            newsSelection.append(article)
            x -= 1
        if x == 0:
            return newsSelection


def displayText(newsSelection, google_news):
    i = 1
    for article in newsSelection:
        with st.spinner("Acessing file #" + str(i)):
            st.write("**File #" + str(i) + ":**")
            article_text = google_news.get_full_article(article['url']).title
            st.write(article_text)
            st.write("------\n")
            i += 1

main()