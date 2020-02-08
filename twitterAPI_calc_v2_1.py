import tweepy
import creds #API LOGIN CREDENTIALS
from gematria_dictv2 import * # DICTIONARIES FOR DIFFERENT TYPES OF GEMATRIA
from gematria_methods_module import *
import time # used for waiting 5 seconds between tweets


# Establishes connection to server and creates the API object
auth = tweepy.OAuthHandler(creds.consumer_key, creds.consumer_secret)
auth.set_access_token(creds.access_token, creds.access_token_secret)
api = tweepy.API(auth)

# Hashtag search, and iterates through the last 20 mentions.
keyword = '#tm3k'
my_mentions = api.mentions_timeline(count=10)
for tweet in my_mentions:
    try:
        line = str(tweet.text) # Converts each mention status to a string so i can manipulate it
        tweet_id = tweet.id # This is a variable grabbing the tweet id from each tweet which is passed into the call to the replyToUsername method below in the loop
        user_id = tweet.user.screen_name # gets user's  twitter @ handle but without the @ symbol ex not @_tm3k but _tm3k
        
        if keyword in line:
            
            temp_var = line.replace('@__tm3k #tm3k', '') # Removes the hashtag and @_tm3k from the phrase and replaces with an empty space so I can sum it up with gematria
            phrase = temp_var.strip()
            phrase.lower() # Strips extra spaces and makes lowercase
            summed_word = getOrdinalGematria(phrase) # Calls gematria sum method and passes the scraped tweet string to be analyzed and stores the result in the variable summed_word
            replyToUsername(tweet_id, summed_word) # Calls reply to username method and passes the id of the tweet containing #tm3k and the value of the letters
            print("Sending reply...\n\n")
            time.sleep(2)
    except:
        print(f"THIS TWEET '{phrase}' HAS ALREADY BEEN REPLIED TO, OR CONTAINS INVALID FORMAT.\n\n")
        continue


# need to re write the code to reply with multiple forms of gematria, and run every 30 seconds in an infinite loop, and run from second laptop
