import twitter

execfile('keys.py')

api = twitter.Api(consumer_key, consumer_secret, access_token_key, access_token_secret)

def GetEntireTimeline(screen_name=None, max_id=None):
    print 'lol no'


