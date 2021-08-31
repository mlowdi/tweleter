import tweepy
from time import sleep

consumer_token = ''
consumer_secret = ''

auth = tweepy.OAuthHandler(consumer_token, consumer_secret)

try:
	redirect_url = auth.get_authorization_url()
except tweepy.TweepError:
	print('Error! No req token.')

print(redirect_url)

verifier = input('Verifier:')

try:
	auth.get_access_token(verifier)
except tweepy.TweepError:
	print('Error! Failed to get access token.')

print("access token:", auth.access_token)
print("access token secret:", auth.access_token_secret)