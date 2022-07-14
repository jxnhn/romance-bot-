import tweepy


auth = tweepy.OAuth1UserHandler('Z7xeyI23AEJdAQFb77cuxMREx',
                                'JZDVJadhrVRcRg53tq6buYHtJtwDEEEdQTiSsyQa45B7XtlNoX',
                                )
auth.set_access_token('1408624157718372352-neK8GvzlpMqC0qULH6vPqjRLQwgbcg',
                      'n7RYgwNyKXRqA00MUVZhmRdqBbzF5sj5vgcGZR7hLiqSc')

api = tweepy.API(auth)


class Listener(tweepy.Stream):
    def on_status(self, status):
        print(status)


stream_tweet = Listener('Z7xeyI23AEJdAQFb77cuxMREx',
                         'JZDVJadhrVRcRg53tq6buYHtJtwDEEEdQTiSsyQa45B7XtlNoX',
                         '1408624157718372352-neK8GvzlpMqC0qULH6vPqjRLQwgbcg',
                         'n7RYgwNyKXRqA00MUVZhmRdqBbzF5sj5vgcGZR7hLiqSc'
                         )
Listener = Listener('Z7xeyI23AEJdAQFb77cuxMREx',
                     'JZDVJadhrVRcRg53tq6buYHtJtwDEEEdQTiSsyQa45B7XtlNoX',
                     '1408624157718372352-neK8GvzlpMqC0qULH6vPqjRLQwgbcg',
                     'n7RYgwNyKXRqA00MUVZhmRdqBbzF5sj5vgcGZR7hLiqSc')

stream = tweepy.Stream(auth = api.auth, listener = Listener)
stream.filter(follow='1168241092636086274')

