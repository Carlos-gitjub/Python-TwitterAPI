import tweepy

consumer_key = 'kqXh5PAmscY9CRVBlWP9Fss7V'
consumer_secret = 'J5oowaDwLlX8ChL2IwKCetnvWrDXnMBlYRHpAd5WPrAmusQ9DJ'

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth)

user = api.get_user('@solrakbot')

for tweet in tweepy.Cursor(api.search, q='tweet 1 kljsfdjklfsda').items(10):
    print(tweet.text)

print('Nombre usuario: ' + user.screen_name)
print('Numero de seguidores: ' + str(user.followers_count))

