#Load dependencies 
import csv
#import openai
from datetime import datetime, timedelta
import time
import os
import pandas as pd

# Function to read CSV and find if there are new new entries

#df = pd.read_csv("data_for_newsletter.csv")

data_for_newsletter_size = 0


def read_csv_and_find_new_entries():

#Check the differences for the initial size. If different, return new size.
        
    print("new index found")
    
    
    
# Function to summarize content using ChatGPT
def summarize_content():
    #openai.api_key = api_key
    #response = openai.Completion.create(
    #    engine="text-davinci-003",
    #    prompt=f"Summarize the following content in {max_length} characters:\n\n{content}",
        #Should have an condition based on the initial vs new csv size
    #)
    print("openai model in action for content_summarize")
    

def summarize_content():
    #openai.api_key = api_key
    #response = openai.Completion.create(
    #    engine="text-davinci-003",
    #    prompt=f"Summarize the following content in {max_length2} characters:\n\n{content}",
        #Should have an condition based on the initial vs new csv size
    #)
    print("openai model in action for content_ready_publish")

    
# Function to update CSV with summarized content
def update_csv_with_summaries():

    print("dataframe updated")
