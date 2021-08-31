#!/usr/bin/env python3

import datetime
import dateutil
import dateutil.parser
import pytz

import tweepy
import json

# Ingests a Twitter archive file, proceeds to delete everything you tweeted before CUTOFF
# NOTE: Doesn't do anything to retweets, how to get rid of those is another project
# Order the archive from your Twitter settings (it takes some time to compile)


# Note: we only really need to set the timezone for comparisons, everything in the Twitter archive is in UTC
CUTOFF = datetime.datetime(2021,6,21,tzinfo=pytz.UTC)

# The file we need is in the data/ folder in your archive
# You will need to maincure it, removing everything before the initial [
# Otherwise the JSON parsser chokes on it
ARCHIVE = 'tweet.js'

# Setup for Twitter API
consumer_token = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''


def missed_tweet(status, error):
	# Small function to yeet any tweet we get an error message for into a file for later processing
	# Error 144 means "Tweet not found" so we can just drop those
	# Anything else may be either a real error or Tweepy throwing a hissy

	if error.api_code == 144:
		print("\tNot saving this status.\n")
		return
	else:
		f = open("missed_status.txt", "a")
		f.write(status['tweet']['id']+"\n")
		f.close
		print("\tMissed status saved!\n")

	#TODO: store this log as JSON, together with error codes, for better processing later


# Get us an API handle
try:
	auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	auth.secure = True
	api = tweepy.API(auth)
except tweepy.TweepError as e:
	raise e
else:
	print("Authenticated with Twitter!")

# Let's get to work!
with open(ARCHIVE) as archive:
	tweets = json.load(archive)
	items = len(tweets)
	index = 0
	for status in tweets:
		index+=1
		idno = status['tweet']['id']
		print(f'Processing status {idno!s} ({index!s}/{items!s})')

		# Here we begin actually deciding what to do with the tweet
		if dateutil.parser.parse(status['tweet']['created_at']) < CUTOFF:

			# Here we catch API errors and log tweets we couldn't delete
			try:
				api.destroy_status(idno)
			except tweepy.TweepError as e:
				print("\t***ERROR:", e.api_code) # Print error code because why not
				missed_tweet(status, e)
			else:
				print(f'\tDeleted status {idno!s}\n')

		# Else: this tweet is a keeper
		else:
			print("\tStatus newer than cutoff, keeping!\n")
