##################
#RC Nov 2017
#Ver. 1
#Usage : Program_name [DEBUG-0/1] [screen_name]
#https://twitter.com/
#from DestroyFriendship_fastversiontest_v2_02 and create_unfollowers_list
#Program to unfollow unfollowers diretly in one step those followed that are not in the fanbaseline
#lastest ver. 1.0
#2017.11.21 12:51
##################
import sys
import tweepy
import csv
from time import sleep
from _credentials import *
#from credentials import *
from random import randint

fansfile='fanbaseline'
DEBUG=False
if len(sys.argv) > 1:
    if sys.argv[1] == '1' :
        print ('args 1 = ' + sys.argv[1])
        DEBUG = True
        print ('DEBUG ON')
if len(sys.argv) == 3:
    target = sys.argv[2]
else:
           target = 'tw_handler'


try:
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
	print ("Reporting Screen Name = " + target)
	friends = api.friends_ids(target)
	followers = []
	for page in tweepy.Cursor(api.followers_ids, target).pages():
		followers.extend(page)
		if len(page) == 5000:
		   sleep(60)
	print ("Followers : " + str(len(followers)))
	print ("Following : " + str(len(friends)))
	print ('id,screen_name,followingme')
	for f in friends:
		if f not in followers:
			if DEBUG:
				print (str(f) + ',' + api.get_user(f).screen_name + ',False')
			if not api.get_user(f).screen_name in open(fansfile).read():
				print ("Unfriend " + api.get_user(f).screen_name)
				if not DEBUG:
					api.destroy_friendship(api.get_user(f).screen_name)
			else:
			     print ("Fan of " + api.get_user(f).screen_name)
except tweepy.TweepError as e:
    print ("tweepy.TweepError=")
    print (e)
    pass
except:
    e = sys.exc_info()
#    #print ('Error:' +  %s + % e )
    print ("Error = " + str(e))
