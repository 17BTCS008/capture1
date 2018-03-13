import os
import time
import tweepy

consumer_key ="Nd1ZtdisQIuYiZ9SIyVnhxd0i"
consumer_secret ="JLwV5KyhNSb3gVjnkDjnuqxQUgoVolccF7GvMVYbt22CDsRO0U"
access_token ="967251581677817857-DxpEmRRD9Q74sdHTOjpcb0nAtMR8jl9"
access_token_secret ="csXN0BKVxPHWnEQioaDGMDGucj9AupKUC531j5qo4PjeX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)  

b=1
a=0

while a<=2:
   
    cmd="fswebcam -F 3 --fps 20 -r 800*600 /home/cs2017a108/Desktop/img.jpg"
    os.system(cmd)
    img="/home/cs2017a108/Desktop/img.jpg"
    print("pic taken")
    api.update_with_media(img, status="nice one")
    print('wait for five seconds for selfie')
    time.sleep(5)
    a+=1
    
    print('success')
          
