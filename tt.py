import tweepy
from datetime import datetime, date
from dateutil.tz import gettz
import time
import json

contenido= open("info.json")
config = json.load(contenido)
estado = config["status"]

api_key = ''
api_secret= ''
bearer_token = f''
access_token = ''
access_token_secret = ''
    

client = tweepy.Client(bearer_token,api_key,api_secret,access_token,access_token_secret)
auth = tweepy.OAuthHandler(api_key, api_secret,access_token,access_token_secret)
api = tweepy.API(auth)

def tweet():
    fecha = date(2023, 3, 10) # fecha en formato año-mes-día
    hoy = date.today() # hoy
    dif = hoy-fecha
    dias_pasados = dif.days
    now = datetime.now(gettz('GMT-4'))
    current_time = now.strftime('%H:%M')

    message = "{}. Hora: {} Dias sin la capsula {}".format(estado,current_time,dias_pasados)
    api.update_status(message)
    print("Tuit enviado!")

tweet()