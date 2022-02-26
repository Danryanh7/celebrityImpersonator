import tweepy
import os

# You can get your access, consumer and bearer tokens from the twitter dev platform but I only used the bearer token
access_token = ''
access_token_secret = ''
consumer_key = ''
consumer_secret = ''
bearer_token = ''

#Grabbing tweets!
username = input("Enter the twitter handle of the user you want to converse with: ")
client = tweepy.Client(bearer_token=bearer_token)
try:
    users = client.get_user(username=username.strip('@'), user_fields=['id'])
    userID = users[0]["id"]
    # Scraping set
    training_set = client.get_users_tweets(id=userID, max_results=100)

    # Write to text file
    os.remove("trainingfile.txt")
    txtfile = open("trainingfile.txt", "a")
    for tweet in training_set.data:
        txtfile.write(str(tweet)+'\n')
except:
    print("Invalid User or Invalid developer token")
    exit()










