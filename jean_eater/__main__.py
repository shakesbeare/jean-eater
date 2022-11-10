import tweepy
import json
import random
import time

from keys import API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

def main():
    auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    while True:
        joke = get_jean_joke()
        try:
            api.update_status(joke)
            print(f"Tweeted joke, {joke}")
        except Exception as e:
            print(f"An error occured: {e}")

        time.sleep(60 * 60 * 24)

def get_jean_joke() -> str:
    with open("jokes.json", "r") as file:
        json_jokes = json.load(file)

    output: str = random.choice(json_jokes["jokes"])
    return output
        
if __name__ == "__main__":
    main()
