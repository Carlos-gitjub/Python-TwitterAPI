import tweepy

consumer_key = 'kqXh5PAmscY9CRVBlWP9Fss7V'
consumer_secret = 'J5oowaDwLlX8ChL2IwKCetnvWrDXnMBlYRHpAd5WPrAmusQ9DJ'



auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth)
for tweet in tweepy.Cursor(api.search, q='tweet 1 kljsfdjklfsda').items(10):
    print(tweet.text)

user = api.get_user('@Solrak45237861')
print(user.screen_name)
print(user.followers_count)

