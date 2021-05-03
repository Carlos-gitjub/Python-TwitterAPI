import tweepy

print('this is my twitter bot')

#Passwords
CONSUMER_KEY = '86bUDs9JMdtbyvI1dqKOW1Z1G'                          
CONSUMER_SECRET = 'wlCzldSmGE54TmxXPFNW3aNPAcYdjk4nKIX0HPpXDnEOByVQ0F' 

BEARER_TOKEN= 'AAAAAAAAAAAAAAAAAAAAAKG6OwEAAAAAxXoSj4mQ4ZfoE8ZFnxCg9%2FgcTIg%3DkcPKHT8j4NVMBK7McfCymdoclNY9T0XYembra7OrtrdtwDaW4G'  #No se usa. La dejo por aquí por si acaso

ACCESS_KEY = '1385643890762518532-4ilMLXwsuzFDRR7jJtmngMIbkh2b7W'  
ACCESS_SECRET = 'Cc7gLGRn4nxAvFFOPTmDbkZ1the1jAnHmHtG6ZX3KFeRS'

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













