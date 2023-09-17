# Quick-Report
A program that takes a user's query and summarizes recent news around that subject!

## About Quick Report
Quick Report is an AI-powered news summarization program created during Hack The North 2023! A user will enter a prompt (a person, event, etc.), Quick Report finds the most recent and relevant news articles for this prompt, and summarizes all of these articles into a single paragraph.

## Inspiration
The main inspiration for this project was that I always had trouble doing research on recent events because different sites and articles would cover different aspects of it. Even with sites like Ground News that showed different perspectives, it was still hard to process all of the different articles.

## How I built it
For this project, I used the GNews library to access the various articles, newspaper3k to access the main texts of each article, and streamlit for the front-end / UI. Then, I used Cohere to summarize each article. I also used Github for version control and preparing for the Devpost submission.

## Challenges I ran into
- **Sourcing the Headlines**
    - Before finding GNews, I struggled with various other sources for news articles, from using NewsAPI (insufficient number of headlines, issue with multi-word prompts) to the "All The News" dataset (most news was old and the file was like 8 GB)
- **RAM & CPU limitations, and repo issues**
    - I tried to use Replit for this project, but the repl constantly buffered due to reaching RAM & CPU limits. Additionally, I had trouble with pulling the repository on Github with the repl.
- **Filtering Articles**
    - Within this list of articles, many were invalid (unable to be summarized) due to several reasons (being NoneType, being too short, etc). An article filtering system had to be implemented as a solution (getTopXArticles function)

## Accomplishments that I'm proud of
- **Github Repository Upkeep**
    - This was the first application where I focused on maintaining the Github repository, ensuring all commits are descriptive and the README is comprehensive. It took a lot of effort to learn the ins and outs of Git, but I believe the results speak for themselves.
- **Full Stack Development**
    - This was the first hackathon where I developed the front and back end of the app by myself! Being able to go from forming an idea to implementing an entire app is an impressive milestone for me, let alone doing it in such a small timeframe.

## What I learned
- **Generative AI - Basics and Techniques**
    - During this hackathon, I learned about and used Voiceflow and Cohere, two products in generative AI. I learned how to use it and how to incorporate as a part of my app through both the workshops and being able to work with these products in a practical application


## What's next for Quick-Report 
- **Add an AI assistant with VoiceFlow**
    - An assistant that uses both text and voice such as the ones Voiceflow offers would be ideal for people who have read the summaries but still have questions
- **Improve Article Search Process**
    - Making the article search process with GNews faster would improve the load times and quality of life of the app
- **Publish App**
    - The next step would be to make this app publicly available such as through a .tech domain  