#Reddit Scraper
#Programmed by Asim Hyder

import praw
import numpy as np
import pandas as pd
import datetime as dt
def ScrapeReddit(subreddit, keyword): #function for scraping a desired subreddit. Will be utilized in the GUI when the Scrape Reddit option is selected. subreddit parameter is the user input for the sub that will be scraped

    reddit = praw.Reddit (client_id = "hsPskyIcTh7EqA" ,
                    client_secret = "GniFoEIRe3W2RLpA8qWrOVt4b8xUOg",
                    username = "448Scraper",
                    password = "Pass448!",
                    user_agent = "ITMS 448 Scraper")

    sub=reddit.subreddit(subreddit) #accesses specified subreddit and stores it in variable sub
    sub_hot = sub.hot(limit = 500) #goes throught the 500 hottest posts in specifed sub reddit that will be scraped
    #array to store the scraped values of each post
    posts_array = {"post_title":[],  #title of post
                    "post_body":[], #body of post
                    "post_author":[], #author of post
                    "post_id":[], #id of post (this was included because the url field returns the url of links in the post, not the post itself, the ID is used in the post url)
                    "comment_num":[], #number of comments
                    "karma":[], #post karma
                    "link":[], #post url
                    "post_date":[]} #date posted

    for submission in sub_hot: #prints the post IDs for the 5 hottest posts in the specified sub
            if keyword in submission.title or submission.selftext: #only appends posts that have the keyword input the user provides
                posts_array["post_title"].append(submission.title)
                posts_array["post_body"].append(submission.selftext)
                posts_array["post_author"].append(submission.author)
                posts_array["post_id"].append(submission.id)
                posts_array["comment_num"].append(submission.num_comments)
                posts_array["karma"].append(submission.score)
                posts_array["link"].append(submission.url)
                posts_array["post_date"].append(dt.datetime.fromtimestamp(submission.created))

    scraped=pd.DataFrame(posts_array)
    scraped.to_csv('%s.csv' %(subreddit), index=False) #exports the array of scraped data to a CSV file

    #np.set_printoptions(threshold=np.inf) #this is here for testing purposes
    #print(posts_array)

#anything below this line is for testing purposes. the function will be implemented in the GUI and not the class iteself
scansub = input("Enter subreddit to scrape: ")
scankey = input("Enter keyword to search for: ")
ScrapeReddit(scansub, scankey)

