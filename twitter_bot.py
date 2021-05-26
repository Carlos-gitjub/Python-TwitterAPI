import tweepy

print('this is my twitter bot')

#Passwords
CONSUMER_KEY = 'jkldsfalkfdalkfdjs'                          
CONSUMER_SECRET = 'klsdfalkjsda' 

BEARER_TOKEN= 'fsdaffdsfasdfafds'  #No se usa. La dejo por aquí por si acaso

ACCESS_KEY = 'fdsafdsafdasdfsdfsdfdsfadfsafd'  
ACCESS_SECRET = 'dsafdsafsdfasdfasdfS'

#Nos logeamos en la API con nuestra cuenta de Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)


################################

#acceder a la API
api = tweepy.API(auth)

#tweeteamos algo
api.update_status('hola cocacola')

#ultima mencion en twitter
mentions = api.mentions_timeline(tweet_mode = 'extended') 
print(mentions[0].text)
#claves del fichero json
print(mentions[0].__dict__.keys())    

#último "me gusta"
print(api.favorites()[0].text)













