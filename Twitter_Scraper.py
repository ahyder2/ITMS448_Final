# Scraper referenced from: https://towardsdatascience.com/how-to-scrape-tweets-from-twitter-59287e20f0f1

# Module imports
import tweepy
from tweepy import OAuthHandler
import pandas as pd
import time

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
search_queries = 'covid OR #covid19 OR covid-19 OR #covid-19 OR coronavirus OR #coronavirus'
tweetCount = 100

# Start runtime
run_start = time.time()

# Twitter scraper function
def scrapeTwitter():
    try:
        # Create tweet query method using API methods and parameters
        tweets = tweepy.Cursor(api.search, q=search_queries).items(tweetCount)

        # Pulling information from tweets iterable object into a tweets list
        tweets_list = [[tweet.id, tweet.user, tweet.text, tweet.user.followers_count, tweet.favorite_count, tweet.retweet_count, tweet.created_at] for tweet in tweets]

        # Create dataframe from tweets list
        tweets_df = pd.DataFrame(tweets_list)

        # Print out data frame of scraped tweets list
        #print(tweets_df)
        tweets_df.to_csv('twitter_covid.csv', index=False)
    except BaseException as e:
        # Error handling
        print('failed to scrape,', str(e))
        time.sleep(3)

    # End runtime
    run_end = time.time()

    # Display runtime duration
    run_duration = round((run_end-run_start)/60, 2)
    print("Scrape runtime:", run_duration)
