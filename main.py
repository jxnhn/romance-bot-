import tweepy
import pandas as pd

<<<<<<< HEAD
# authentication
auth = tweepy.OAuth1UserHandler('api_key', 'api_key_secret')
auth.set_access_token('access_token', 'access_token_secret')
=======
auth = tweepy.OAuth1UserHandler('my_keys',
                                'keys',
                                )
auth.set_access_token('keys',
                      'keys')
api = tweepy.API(auth)


# criando uma lista vazia de tweets

def get_tweets(tweet):
    tweets = []
>>>>>>> bb93fff8c47de64f6b57fba79bbf0b514a114f75

api = tweepy.API(auth)

# user tweets
user = 'smirellii'
limit=300

tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)

# tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')

# create DataFrame
columns = ['User', 'Tweet']
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)

print(df)






