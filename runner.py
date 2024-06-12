import web_scrapping
import wrap_up
import summarizer
import data_uploader

import schedule
import time

def job1():
    # Step 1: Scrape articles
    articles = web_scrapping.get_articles_from_fiercehealthcare()
    print("Job 1 completed: Articles scraped.")

def job2():
    # Step 2: Wrap up articles (assumes articles are stored or passed correctly)
    wrapped_articles = wrap_up.wrap(articles)
    print("Job 2 completed: Articles wrapped.")

def job3():
    # Step 3: Summarize articles (assumes wrapped articles are stored or passed correctly)
    summaries = summarizer.summarize(wrapped_articles)
    print("Job 3 completed: Articles summarized.")

def job4():
    # Step 4: Upload data (assumes summaries are stored or passed correctly)
    data_uploader.upload(summaries)
    print("Job 4 completed: Articles uploaded.")

# Schedule each job to run every hour with a 10-minute stagger between them
schedule.every().hour.at(":00").do(job1)
schedule.every().hour.at(":10").do(job2)
schedule.every().hour.at(":20").do(job3)
schedule.every().hour.at(":30").do(job4)

while True:
    schedule.run_pending()
    time.sleep(1)