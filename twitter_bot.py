import tweepy
import json

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


tweet_list=[]
class MyStreamListener(tweepy.StreamListener):
    def __init__(self,api=None):
        super(MyStreamListener,self).__init__()
        self.num_tweets=0
        self.file=open("tweet.txt","w")
    def on_status(self,status):
        tweet=status._json
        self.file.write(json.dumps(tweet)+ '\n')
        tweet_list.append(status)
        self.num_tweets+=1
        if self.num_tweets<1000:
            return True
        else:
            return False
        self.file.close()

        #create streaming object and authenticate
l = MyStreamListener()
stream =tweepy.Stream(auth,l)
#this line filters twiiter streams to capture data by keywords
stream.filter(track=['covid','corona','covid19','coronavirus',
'facemask','sanitizer','social-distancing'])


tweets_data_path='copp.txt'              #file con la INFO
tweets_data=[]                           #formato json
tweets_file=open(tweets_data_path,"r")   #lector
#read in tweets and store on list
for line in tweets_file:
    tweet=json.loads(line)
    tweets_data.append(tweet)
tweets_file.close()
print(tweets_data[0])




