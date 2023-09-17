# Quick-Report
A program that takes a user's query and summarizes recent news around that subject!

## About Quick Report
Quick Report is an AI-powered news summarization program! A user will enter a prompt (a person, event, etc.), Quick Report finds the most recent and relevant news articles for this prompt, and summarizes all of these articles into a single paragraph.

## Inspiration
The main inspiration for this project was that I always had trouble doing research on recent events because different sites and articles would cover different aspects of it.

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
- Problem Solving
- Github Repository Upkeep


## What we learned

## What's next for Quick-Report (temporary to-do list for the hackathon)
- ~~Add Cohere AI summarizing the articles~~
- ~~Add the full summary (combining the summaries smoothly)~~
- Add AI voiceover using Voiceflow
- Turn this into a .tech domain
- Add css colour changes (optional)
- Polish project(UI/UX, appearance, etc.)
- Finish Github README.md & Devpost story
- Make the Article searching / summarization process faster