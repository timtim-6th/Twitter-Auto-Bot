import tweepy

# Replace with your own API keys and access tokens
consumer_key = " "
consumer_secret = " "
access_token = " "
access_token_secret = " "

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create a Tweepy API object
api = tweepy.API(auth)

# Your tweet content
tweet_text = "Hello, Twitter! This is not a test tweet from my Twitter bot. #NotaTwitterBot #Automationnen"

# Post a tweet
api.update_status(status=tweet_text)

print("Tweet posted successfully!")
