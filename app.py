#this currently uses streamlit as the UI / "Frontend"
import streamlit as st
from gnews import GNews
import datetime


def main():

    st.set_page_config(page_title="Quick Report",
                       page_icon=":rolled_up_newspaper:")
    st.header("Quick Report :rolled_up_newspaper:")

    subject = st.text_input('**Choose a Subject to Summarize:**')

    st.write("Subject: " + subject)

    with st.spinner("Getting articles..."):
        google_news = GNews()
        news = google_news.get_news(subject)
    st.write("Found " + str(len(news)) + " articles")
    st.write(news[0])
    # for article in news:
        # st.write(article['title'])

    
main()