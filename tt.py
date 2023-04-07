import tweepy
from datetime import datetime
from dateutil.tz import gettz
import time


api_key = ''
api_secret= ''
bearer_token = f''
access_token = ''
access_token_secret = ''

client = tweepy.Client(bearer_token,api_key,api_secret,access_token,access_token_secret)
auth = tweepy.OAuthHandler(api_key, api_secret,access_token,access_token_secret)
api = tweepy.API(auth)

def tweet():
    now = datetime.now(gettz('GMT-4'))
    current_time = now.strftime('%H:%M')

    message = "NO. Hora: {}".format(current_time)
    api.update_status(message)
    print("Tuit enviado!")


while True:
    tweet()
    time.sleep(1800)