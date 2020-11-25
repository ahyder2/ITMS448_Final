#Reddit Scraper
#Programmed by Asim Hyder

import praw

def ScrapeReddit(subreddit): #function for scraping a desired subreddit. Will be utilized in the GUI when the Scrape Reddit option is selected. subreddit parameter is the user input for the sub that will be scraped

    reddit = praw.Reddit (client_id = "hsPskyIcTh7EqA" ,
                    client_secret = "GniFoEIRe3W2RLpA8qWrOVt4b8xUOg",
                    username = "448Scraper",
                    password = "Pass448!",
                    user_agent = "ITMS 448 Scraper")

    sub=reddit.subreddit(subreddit) #accesses specified subreddit and stores it in variable sub
    sub_hot = sub.hot(limit = 5) #goes throught the 5 hottest posts in specifed sub reddit that will be scraped

    for submission in sub_hot: #prints the post IDs for the 5 hottest posts in the specified sub
        print(submission) #this will be updated for more sophisticated functionality. currently here for testing purposes

#anything below this line is for testing purposes. the function will be implemented in the GUI and not the class iteself
scansub = input("Enter subreddit to scrape: ")
ScrapeReddit(scansub)

