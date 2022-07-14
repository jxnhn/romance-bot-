import tweepy
import random

auth = tweepy.OAuth1UserHandler('my_keys',
                                'keys',
                                )
auth.set_access_token('keys',
                      'keys')
api = tweepy.API(auth)


# criando uma lista vazia de tweets

def get_tweets(tweet):
    tweets = []

# Listinha de respostas, sorteando uma delas pra responder.

def reply():
    respostas = ["eu te amo muito sua gostosa", "voce e o amor da minha vida sabia",
                     "concordo vamos casar", "LINDAAAAAA AAAAAAAAAAAA AAAAAAAAAAAA"]
    which_one = random.randint(0, 3)
    api.update_status(f'@smirellii {respostas[which_one]}')


# pegar os tweet e responder

user = 'smirellii'
mi = api.user_timeline(user_id = 1168241092636086274)
mi_tweets = get_tweets(mi)
reply(mi_tweets)










