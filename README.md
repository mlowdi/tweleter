# BEHOLD, THE JANK

So I realized I wanted to get rid of some old tweets, but I have a lot of them. And [Yuri Tweet Deleter](https://github.com/fellipec/YuriTweetDeleter/) has stopped working since Twitter moved from CSV to JSON format in the archive downloads. And all the other options are either shady, want you to pay to have more than ~3k tweets deleted - or they are great but just can't do what I wanted (shoutout [Semiphemeral](https://semiphemeral.com/) y'all are great but I needed The Big Guns.)

So I hacked up this script because "Janky Solutions" is my middle name.

## How it works

1. Download your archive from Twitter
2. Manicure `data/tweet.js` by stripping everything before the opening `[`
3. Get all the required tokens from Twitter and paste them into the correct variables in the tweleter script
    + I have no idea how you get the consumer tokens from Twitter these days, I'm still using creds from 2012, sorry
    + Once you have the consumer tokens can use the oauther script to run the auth process and generate access tokens for a specific user
    + The official [Tweepy auth tutorial](https://docs.tweepy.org/en/stable/auth_tutorial.html) might be useful as a reference
4. Stick the .js file in the tweleter folder
5. Run the script and watch the magic happen. Slowly.

The rest of the "documentation" is in the code comments. Lol.

## Requirements

You need Python 3.something - it works on 3.6.9. I wrote this on a Windows machine with an Ubuntu 18.04 WSL install, so I'm decidedly *not* cutting edge.

Then you need some Python packages:

- Tweepy
- Dateutil
- PyTZ

They're all available in `pip` and I'm sure there are both better options and better ways of getting them but as you might imagine this isn't exactly my day job and I have no idea how anything works.
