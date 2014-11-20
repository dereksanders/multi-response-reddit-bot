import praw
import time
from random import random

def makeResponseArray(replies, weights):
    responseArray = []
    i = 0

    while i < len(replies):
        responseArray.append([replies[i], weights[i]])
        i += 1

    return responseArray

def calcWeightSum(responseArray):
    i = 0
    weightSum = 0

    while i < len(responseArray):
        weightSum += responseArray[i][1]
        i += 1

    return weightSum

def makeProbArray(responseArray, weightSum):
    i = 1;
    
    probArray = [responseArray[0][1] / weightSum]

    print(probArray[0])

    while i < len(responseArray):
        probArray.append(probArray[i-1] + (responseArray[i][1] / weightSum))
        print(probArray[i])
        i += 1

    return probArray

def findComment(subreddit, hotwords, responseArray, probArray):

    already_done = set()
    lastMsg = -1

    while True:
         for comment in subreddit.get_comments():
            print(comment)
            time.sleep(0.5) #This is for debugging purposes; remove it to quicken process
            has_hot = any(string in comment.body for string in hotwords)
            
            if has_hot and comment.id not in already_done: 
                replySelect = random()
                lastMsg = postReply(comment, responseArray, probArray, replySelect, lastMsg)
                already_done.add(comment.id) #Records ID of comment replied to; will not reply to the same comment twice
                time.sleep(600) #Waits until bot may post again

def postReply(comment, responseArray, probArray, replySelect, lastMsg):
    replyPosted = 0
    i = 0

    while replyPosted == 0:
        if replySelect <= probArray[i] and i != lastMsg:
            comment.reply(responseArray[i][0])
            print("Comment posted: " + responseArray[i][0])
            lastMsg = i
            replyPosted = 1
            
        if i < len(probArray) - 1:
            i += 1
            
        else:
            replySelect = random()
            i = 0

    print(lastMsg)
    return lastMsg
