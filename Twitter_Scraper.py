# Scraper referenced from: https://towardsdatascience.com/how-to-scrape-tweets-from-twitter-59287e20f0f1

# Module imports
import tweepy
from tweepy import OAuthHandler
import pandas as pd

# Twitter credentials from Twitter Developer account
api_key = "g5r9YJDGt9f1DqbdJBIzok5fU"
api_key_secret = "DQE0tfUnyoI7j3Jy1O8VfCLlFnhBExRPY7RW8d469H5q8rmScx"
access_token = "1330984194395213826-dDj2QPZRVW3jsBG0XsRlZRTs51JUUo"
access_token_secret = "tObYnmAVyV2esNm7cD0feC6SBHEqDw76j1nRkhcLKt1OC"

# Tweepy twitter authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Search query and tweet count parameters
search_queries = 'covid OR #covid19'
tweetCount = 1

try:
    # Creation of query method using parameters
    tweets = tweepy.Cursor(api.search, q=search_queries).items(tweetCount)

    # Pulling information from tweets iterable object
    tweets_list = [[tweet.id, tweet.text, tweet.user, tweet.user.followers_count, tweet.favorite_count, tweet.retweet_count, tweet.created_at] for tweet in tweets]

    # Creation of dataframe from tweets list
    # Add or remove columns as you remove tweet information
    tweets_df = pd.DataFrame(tweets_list)

    # Print out scraped tweets list
    print(tweets_list)
 
except BaseException as e:
    # Error handling
    print('failed to scrape,', str(e))
    time.sleep(3)