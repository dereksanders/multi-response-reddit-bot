import praw
from botFunctions import *

r = praw.Reddit('Multi-Response Reddit Bot')

#Define relevant log-in details here

username = 'username'
password = 'password'

r.login(username, password)

subreddit = r.get_subreddit('test') #Choose subreddit in which you wish to post

subreddit_comments = subreddit.get_comments()

hotwords = ['the', 'and', 'a'] #Words/phrases that will elicit a response from the bot

already_done = set()

print('Initializing...')

#Define the bot's comments and their weights (likeliness of a particular reply in relation to others)

com1 = 'comment1.'
w1 = 1

com2 = 'comment2.'
w2 = 1

com3 = 'comment3.'
w3 = 0.5

com4 = 'comment4.'
w4 = 2

com5 = 'comment5.'
w5 = 1

replies = [com1, com2, com3, com4, com5]
weights = [w1, w2, w3, w4, w5]

responseArray = makeResponseArray(replies, weights)

probArray = makeProbArray(responseArray, calcWeightSum(responseArray))

findComment(subreddit, hotwords, responseArray, probArray)
