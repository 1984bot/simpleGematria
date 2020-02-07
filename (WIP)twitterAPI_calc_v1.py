import tweepy
import creds #API LOGIN CREDENTIALS
from gematria_dictv2 import * # DICTIONARIES FOR DIFFERENT TYPES OF GEMATRIA

# Establishes connection to server and creates the API object
auth = tweepy.OAuthHandler(creds.consumer_key, creds.consumer_secret)
auth.set_access_token(creds.access_token, creds.access_token_secret)
api = tweepy.API(auth)

# Method for determining gematria
def getGematria(phrase):
    total = 0
    for c in phrase:
        ordinal = ord(c) - 96
        print('{} = {}'.format(c, ordinal))
        total += ordinal
        
    print('Your phrase ordinal gematria sum is: {}\n'.format(total))

# Hashtag search, and iterates through the last 20 mentions.
keyword = '#tm3k'
my_mentions = api.mentions_timeline()
for tweet in my_mentions:
    line = str(tweet.text) # Converts each mention status to a string so i can manipulate it

    if keyword in line:
        temp_var = line.replace('@_tm3k #tm3k', '') #Removes the hashtag and @_tm3k from the phrase and replaces with an empty space so I can sum it up with gematria
        phrase = temp_var.lstrip()
        print(phrase)
        phrase.lower() #Strips extra spaces and makes lowercase
        
        summed_word = getGematria(phrase) #Calls gematria sum method and passes the scraped tweet string to be analyzed 
        
