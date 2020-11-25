#Reddit Scraper
#Programmed by Asim Hyder

import praw

#def ScrapeReddit(subreddit):

reddit = praw.Reddit (client_id = "hsPskyIcTh7EqA" ,
                client_secret = "GniFoEIRe3W2RLpA8qWrOVt4b8xUOg",
                username = "448Scraper",
                password = "Pass448!",
                user_agent = "ITMS 448 Scraper")

print(reddit.user.me())