# celebrityImpersonator
Capstone Project for 'Build Chatbots with Python'. 

## Premise
A Twitter scraper that parses celebrity tweets and trains an AI on how it may speak like them.
Tweepy allows a maximum of 100 pulled tweets at any given time, which limits the data set available.

## Implementation
Used NLP to preproccess parsed celebrity tweets to generate a seq2seq model.
I decided to use an open-domain chatbot to give the chatbot more flexibillity in it's responses and so that I may gain experience training an AI.

## Concerns and Known Issues
The model is prone to overfitting
This version of tensorflow is slow to train on a CPU
It may be considered immoral to replicate the speech of another. However, this bot is limited to highlighting tropes and commonly used words in one's speech patterns.
Only 100 tweets were able to be captured at once

## Dependencies
Tensorflow (tf.keras + LSTM, Dense (softmax))
Tweepy
Regex
numpy
