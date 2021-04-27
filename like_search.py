import tweepy

#Passwords
CONSUMER_KEY = '86bUDs9JMdtbyvI1dqKOW1Z1G'                          
CONSUMER_SECRET = 'wlCzldSmGE54TmxXPFNW3aNPAcYdjk4nKIX0HPpXDnEOByVQ0F' 

BEARER_TOKEN= 'AAAAAAAAAAAAAAAAAAAAAKG6OwEAAAAAxXoSj4mQ4ZfoE8ZFnxCg9%2FgcTIg%3DkcPKHT8j4NVMBK7McfCymdoclNY9T0XYembra7OrtrdtwDaW4G'  #No se usa. La dejo por aquí por si acaso

ACCESS_KEY = '1385643890762518532-4ilMLXwsuzFDRR7jJtmngMIbkh2b7W'  
ACCESS_SECRET = 'Cc7gLGRn4nxAvFFOPTmDbkZ1the1jAnHmHtG6ZX3KFeRS'

#Nos logeamos en la API con nuestra cuenta de Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

#Creamos la variable para acceder a la API
api = tweepy.API(auth)

#
#
#
#
#
#
#
#
#
#

def like_search():
    clave = input('Palabras clave a buscar: ')
    favorites = api.favorites()  #fichero json con los datos de todos los me gusta
    for i in range(10,0,-1):
        print(favorites[i].text)
like_search()




