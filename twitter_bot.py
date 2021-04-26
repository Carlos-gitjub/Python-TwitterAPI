import tweepy

print('this is my twitter bot')

#Passwords
CONSUMER_KEY = 'kqXh5PAmscY9CRVBlWP9Fss7V'                          
CONSUMER_SECRET = 'J5oowaDwLlX8ChL2IwKCetnvWrDXnMBlYRHpAd5WPrAmusQ9DJ' 

ACCESS_KEY = 'AAAAAAAAAAAAAAAAAAAAAKG6OwEAAAAAaGLczQiWHKWhy6DQPTQhwV1WPXo%3D5T4q'
ACCESS_SECRET = 'NxHyei5QUjzsVFbqYV5BXLfh38Mez6BODHPd64r8kHFccS'

#Nos logeamos en la API con nuestra cuenta de Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#Creamos la variable para acceder a la API
api = tweepy.API(auth)

#Ejemplo: tweeteamos algo
api.update_status('hola cocacola')
