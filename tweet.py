# -*- coding: utf-8 -*-

import random
import tweepy

#Datos de https://apps.twitter.com/app/new
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#Abro el archivo
archivo = open("tweets.txt","r").readlines()

#Busca cual linea leera y la actualiza en twitter
api.update_status(archivo[random.randint(0,len(archivo)-1)])
