import tweepy
import json

# KEY SOURCE
keys = json.load(open("keys.json"))

CONSUMER_KEY = keys["CONSUMER_KEY"]
CONSUMER_SECRET = keys["CONSUMER_SECRET"]
ACCESS_TOKEN = keys["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = keys["ACCESS_TOKEN_SECRET"]

client = tweepy.Client(consumer_key=CONSUMER_KEY,
                       consumer_secret=CONSUMER_SECRET,
                       access_token=ACCESS_TOKEN,
                       access_token_secret=ACCESS_TOKEN_SECRET
                       )

while True:
    print("What's happening?")
    text = input()

    confirm = input(f'Are you sure you want to Tweet "{text}" (Y/N) ')

    if confirm.upper() == 'Y':
        print("Sent!")
        client.create_tweet(text=text)
        break
