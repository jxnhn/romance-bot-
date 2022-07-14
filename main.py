import tweepy


# autenticação

auth = tweepy.OAuth1UserHandler('consumer', 'consumer secret')
auth.set_access_token('acess',
                      'acess secret')
api = tweepy.API(auth)

# criando uma stream

stream = tweepy.Stream('consumer',
                       'consumer secret',
                       'acess',
                       'acess secret')


class MiListener(tweepy.Stream):

    def on_status(self, status):
        print(status)
        api.update_status("oii", in_reply_to_status_id=1408624157718372352)


MiListener = MiListener(
    "consumer", "consumer secret",
    "acess", "acess secret"
)
MiListener.filter(follow=[1408624157718372352], threaded=True)





