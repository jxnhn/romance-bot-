import tweepy


# autenticação

auth = tweepy.OAuth1UserHandler('syzR2OG9T426CndeJHXawljey', 'wFvstaHRYxH5sQc7nvd962oPHfIFUwNAnt7qx2oTvgJJPoDkyq')
auth.set_access_token('1408624157718372352-ejkMgOA6s5A8fYbzVAgO0E0muCjC2U',
                      'vQ38rOItfogW21KpzWkZ7fuaCrnP0TNuZOh8uxD4UzTic')
api = tweepy.API(auth)

# criando uma stream

stream = tweepy.Stream('syzR2OG9T426CndeJHXawljey',
                       'wFvstaHRYxH5sQc7nvd962oPHfIFUwNAnt7qx2oTvgJJPoDkyq',
                       '1408624157718372352-ejkMgOA6s5A8fYbzVAgO0E0muCjC2U',
                       'vQ38rOItfogW21KpzWkZ7fuaCrnP0TNuZOh8uxD4UzTic')


class MiListener(tweepy.Stream):

    def on_status(self, status):
        print(status)
        api.update_status("oii", in_reply_to_status_id=1408624157718372352)


MiListener = MiListener(
    "syzR2OG9T426CndeJHXawljey", "wFvstaHRYxH5sQc7nvd962oPHfIFUwNAnt7qx2oTvgJJPoDkyq",
    "1408624157718372352-ejkMgOA6s5A8fYbzVAgO0E0muCjC2U", "vQ38rOItfogW21KpzWkZ7fuaCrnP0TNuZOh8uxD4UzTic"
)
MiListener.filter(follow=[1408624157718372352], threaded=True)





