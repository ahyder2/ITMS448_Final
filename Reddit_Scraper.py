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
    #array to store the scraped values of each post
    posts_array = {"post_title":[], #title of post
                    "post_body":[], #body of post
                    "comment_num":[], #number of comments
                    "karma":[], #post karma
                    "link":[], #post url
                    "post_date":[]} #date posted

    for submission in sub_hot: #prints the post IDs for the 5 hottest posts in the specified sub
        if not submission.stickied: #doesn't scrape sitckied posts
            posts_array["post_title"].append(submission.title)
            print(posts_array[0])
            posts_array["post_body"].append(submission.selftext)
            print(posts_array[1])
            posts_array["comment_num"].append(submission.num_comments)
            print(posts_array[2])
            posts_array["karma"].append(submission.score)
            print(posts_array[3])
            posts_array["link"].append(submission.url)
            print(posts_array[4])
            posts_array["post_date"].append(submission.created)
            print(posts_array[5])

#anything below this line is for testing purposes. the function will be implemented in the GUI and not the class iteself
scansub = input("Enter subreddit to scrape: ")
ScrapeReddit(scansub)

