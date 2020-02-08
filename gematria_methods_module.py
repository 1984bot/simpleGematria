from gematria_dictv2 import *

# Method for determining who it was that is requesting a tweet and replying to it with summed_word
def replyToUsername(tweet_id,summed_word):
    
    #This code prints basic info to console so i can follow what the program is doing mentally and to double check that each value is assigned accordingly
    print(f'Tweet Id: {tweet_id}')
    print(f'Phrase: {phrase}')
    print(f'{summed_word}')
    print(f'Screen name: {tweet.user.name}')
    print(f'Username: {user_id}')

    api.update_status(summed_word, in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)

# Medthod to check if numbers are in the phrase
def hasNumbers(phrase):
    return any(char.isdigit() for char in phrase)

# Method to determine ordinal gematria
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

# Method to determine full reduction gematria
def getFullReductionGematria(phrase):

    total = []
    for n in phrase:
        
        if n == 'a':
            total.append(1)
            
        elif n == 'b':
            total.append(2)
            
        elif n == 'c':
            total.append(3)
            
        elif n == 'd':
            total.append(4)
            
        elif n == 'e':
            total.append(5)
        
        elif n == 'f':
            total.append(6)
            
        elif n == 'g':
            total.append(7)
            
        elif n == 'h':
            total.append(8)
            
        elif n == 'i':
            total.append(9)
            
        elif n == 'j':
            total.append(1)
            
        elif n == 'k':
            total.append(2)
            
        elif n == 'l':
            total.append(3)
           
        elif n == 'm':
            total.append(4)
            
        elif n == 'n':
            total.append(5)
            
        elif n == 'o':
            total.append(6)
            
        elif n == 'p':
            total.append(7)
            
        elif n == 'q':
            total.append(8)
            
        elif n == 'r':
            total.append(9)
            
        elif n == 's':
            total.append(1)
            
        elif n == 't':
            total.append(2)
            
        elif n == 'u':
            total.append(3)
            
        elif n == 'v':
            total.append(4)
            
        elif n == 'w':
            total.append(5)
            
        elif n == 'x':
            total.append(6)
            
        elif n == 'y':
            total.append(7)
            
        elif n == 'z':
            total.append(8)
            
    sumtotal = sum(total)
        

        

    
    return_value = "Full reduction gematria: {}".format(sumtotal)
    return return_value