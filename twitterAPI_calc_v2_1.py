import tweepy
import creds #API LOGIN CREDENTIALS
from gematria_dictv2 import * # DICTIONARIES FOR DIFFERENT TYPES OF GEMATRIA
import time # used for waiting 5 seconds between tweets

# Medthod to check if numbers are in the phrase
def hasNumbers(phrase):
    return any(char.isdigit() for char in phrase)

# Method for determining ordinal gematria
def getOrdinalGematria(phrase):
    total = 0
    
    # First check to see if the phrase contains any numbers
    if hasNumbers(phrase):
        pass
    else:

        stripped_phrase = phrase.replace(" ", "") #replaces all spaces with nothing
        for c in stripped_phrase:
            ordinal = ord(c) - 96
            total += ordinal    
        reply_tweet = "Ordinal gematria: {}".format(total)
        return reply_tweet

# Method for determining full reduction gematria
#def getFullReductionGematria(phrase):


# Method for determining who it was that is requesting a tweet and replying to it with summed_word
def replyToUsername(tweet_id,summed_word):
    
    #This code prints basic info to console so i can follow what the program is doing mentally and to double check that each value is assigned accordingly
    print(f'Tweet Id: {tweet_id}')
    print(f'Phrase: {phrase}')
    print(f'{summed_word}')
    print(f'Screen name: {tweet.user.name}')
    print(f'Username: {user_id}')

    api.update_status(summed_word, in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)

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
