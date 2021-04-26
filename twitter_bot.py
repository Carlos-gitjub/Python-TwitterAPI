import tweepy

print('this is my twitter bot')

CONSUMER_KEY = 'kqXh5PAmscY9CRVBlWP9Fss7V'                          # 'dxRifUFHDsJFMG1ZF4R0IlHZo'
CONSUMER_SECRET = 'J5oowaDwLlX8ChL2IwKCetnvWrDXnMBlYRHpAd5WPrAmusQ9DJ' #'9llzT36hmcDRogO3tKTunnEdHTAWjVRX5du4ewENR4dTqUF47n'
ACCESS_KEY = 'AAAAAAAAAAAAAAAAAAAAAKG6OwEAAAAAaGLczQiWHKWhy6DQPTQhwV1WPXo%3D5T4q'
ACCESS_SECRET = 'NxHyei5QUjzsVFbqYV5BXLfh38Mez6BODHPd64r8kHFccS'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

api.update_status('Twitter reporting in live')
