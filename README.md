# celebrityImpersonator
Capstone Project for Codecademy's 'Build Chatbots with Python'. 

## Premise
* A Twitter scraper that parses celebrity tweets and trains an AI on how it may speak like them.
* Tweepy allows a maximum of 100 pulled tweets at any given time, which limits the data set available.

## Implementation
* Used NLP to preproccess parsed celebrity tweets to generate a seq2seq model.
* I decided to use an open-domain chatbot to give the chatbot more flexibillity in it's responses and so that I may gain experience training an AI.

## Concerns and Known Issues
* The model is prone to overfitting
* This version of tensorflow is slow to train on a CPU
* It may be considered immoral to replicate the speech of another. However, this bot is limited to highlighting tropes and commonly used words in one's speech patterns.
* Only 100 tweets were able to be captured at once

## Dependencies
* Tensorflow (tf.keras + LSTM, Dense (softmax))
* Tweepy
* Regex
* numpy
* Twitter Bearer Token

# Models

### Scraped Tweets From Training File
![Screen Shot 2022-03-25 at 4 31 11 PM](https://user-images.githubusercontent.com/89366190/160196797-0c8bb179-47c3-4f86-8244-167d06698c37.png)

### Requesting Twitter Handle
![Screen Shot 2022-03-25 at 4 30 48 PM](https://user-images.githubusercontent.com/89366190/160196803-65ff3bb4-379a-4396-87bf-6385c85f4a45.png)

### Training Model
![Screen Shot 2022-03-25 at 4 29 19 PM](https://user-images.githubusercontent.com/89366190/160196807-f49d686d-1805-4ebf-9f71-c4ff8afcf0e1.png)

### Talking to Bot (You can notice pattern similarities especially with emoji use)
![Screen Shot 2022-03-25 at 4 30 08 PM](https://user-images.githubusercontent.com/89366190/160196813-77e878a6-9c53-4bff-a12a-48e9ce23f379.png)
