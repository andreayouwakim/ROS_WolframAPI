#!/usr/bin/env python

#See the readme for how to install wolframalpha 
#onto your machine.
import wolframalpha

#this is the message prompt for the user
input = raw_input("Question: ")

#this is my app id used to send queries to 
#wolfram alpha.
app_id = "3WVVWU-W3A54PVHHY"

#this line sets up the transportation system
#of the question to wolfram alpha
client = wolframalpha.Client(app_id)

#this sends the query off to wolfram alpha
res = client.query(input)

#parsing the pods from the answer to clean up response
answer = next(res.results).text

#printing the cleaned result
print answer
