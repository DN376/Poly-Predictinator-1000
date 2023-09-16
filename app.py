#this currently uses streamlit as the UI / "Frontend"
import streamlit as st
from newsapi import NewsApiClient
import datetime


def main():

    st.set_page_config(page_title="Quick Report",
                       page_icon=":rolled_up_newspaper:")
    st.header("Quick Report :rolled_up_newspaper:")

    subject = st.text_input('**Choose a Subject to Summarize:**')

    st.write("Subject: " + subject)

    


main()