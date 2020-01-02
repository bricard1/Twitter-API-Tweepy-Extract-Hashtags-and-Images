import tweepy

#you'll need to register with Twitter API and get your own keys to place here
consumer_key="***"
consumer_secret="***"
access_token="***"
access_token_secret="***"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit_notify =True, wait_on_rate_limit=True)
import time
import random
searched_tweets = []
last_id = 100000
max_tweets=100000000000

#put your own hashtags here 
hashtags = ["#List","#Of", "#hashtags"]
for i in hashtags:
    query=i
    print("Query: ",query)
    try:
        new_tweets = api.search(q=query,tweet_mode='extended')
        searched_tweets.extend(new_tweets)
        for tweet in new_tweets:
            if not tweet.retweeted:
                print("Text:",tweet.full_text.encode('utf-8'))
                print("Created_at:",tweet.created_at)
                print("ID:",tweet.id)
                if 'media' in tweet.entities:
                    for image in  tweet.entities['media']:
                        print("Mediaurl:",image['media_url'])
                    else:
                        pass
    except tweepy.TweepError as e:
        print("Error: error!")
        time.sleep(25)
#This script will run and get all availible tweets with the query from the last 7 days (per Twitter's API restriction)
