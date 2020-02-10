import tweepy
import creds #API LOGIN CREDENTIALS
from gematria_dictv2 import * # DICTIONARIES FOR DIFFERENT TYPES OF GEMATRIA
import time # used for waiting 5 seconds between tweets
import re # used to strip out non-alphabetic characters

# Medthod to check if numbers are in the phrase
def hasNumbers(phrase):
    return any(char.isdigit() for char in phrase)

# Method for determining gematria
def getGematria(phrase):
    total = 0
    
    # First check to see if the phrase contains any numbers
    if hasNumbers(phrase):
        pass
    else:

        for c in phrase:
            ordinal = ord(c) - 96
            total += ordinal    
        
        
        total2 = []
        for n in phrase:
            
            if n == 'a':
                total2.append(1)
                
            elif n == 'b':
                total2.append(2)
                
            elif n == 'c':
                total2.append(3)
                
            elif n == 'd':
                total2.append(4)
                
            elif n == 'e':
                total2.append(5)
            
            elif n == 'f':
                total2.append(6)
                
            elif n == 'g':
                total2.append(7)
                
            elif n == 'h':
                total2.append(8)
                
            elif n == 'i':
                total2.append(9)
                
            elif n == 'j':
                total2.append(1)
                
            elif n == 'k':
                total2.append(2)
                
            elif n == 'l':
                total2.append(3)
               
            elif n == 'm':
                total2.append(4)
                
            elif n == 'n':
                total2.append(5)
                
            elif n == 'o':
                total2.append(6)
                
            elif n == 'p':
                total2.append(7)
                
            elif n == 'q':
                total2.append(8)
                
            elif n == 'r':
                total2.append(9)
                
            elif n == 's':
                total2.append(1)
                
            elif n == 't':
                total2.append(2)
                
            elif n == 'u':
                total2.append(3)
                
            elif n == 'v':
                total2.append(4)
                
            elif n == 'w':
                total2.append(5)
                
            elif n == 'x':
                total2.append(6)
                
            elif n == 'y':
                total2.append(7)
                
            elif n == 'z':
                total2.append(8)
                
        total2sum = sum(total2)


        reply_tweet = "Ordinal sum: {}\nFull reduction sum: {}".format(total,total2sum)
        return reply_tweet

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


while True:
    # Hashtag search, and iterates through the last 20 mentions.
    keyword = '#tm3k'
    my_mentions = api.mentions_timeline(count=40)
    for tweet in my_mentions:
        try:
            line = str(tweet.text) # Converts each mention status to a string so i can manipulate it
            tweet_id = tweet.id # This is a variable grabbing the tweet id from each tweet which is passed into the call to the replyToUsername method below in the loop
            user_id = tweet.user.screen_name # gets user's  twitter @ handle but without the @ symbol ex not @_tm3k but _tm3k
            
            if keyword in line:
                
                temp_var = line.replace('@__tm3k #tm3k', '') # Removes the hashtag and @_tm3k from the phrase and replaces with an empty space so I can sum it up with gematria
                phrase = re.sub('[^a-zA-Z]', '', temp_var) # Strip all non-alphabetic characters
                phrase = phrase.lower() # Make lowercase
                summed_word = getGematria(phrase) # Calls gematria sum method and passes the scraped tweet string to be analyzed and stores the result in the variable summed_word
                replyToUsername(tweet_id, summed_word) # Calls reply to username method and passes the id of the tweet containing #tm3k and the value of the letters
                print("Sending reply...\n\n")
                time.sleep(10)
        except:
            print(f"THIS TWEET '{phrase}' HAS ALREADY BEEN REPLIED TO, OR CONTAINS INVALID FORMAT.\n\n")
            time.sleep(10)
            continue
