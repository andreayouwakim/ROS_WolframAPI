#!/usr/bin/env python
import wolframalpha

input = raw_input("Question: ")
app_id = "3WVVWU-W3A54PVHHY"

client = wolframalpha.Client(app_id)

res = client.query(input)
answer = next(res.results).text
#print res
print answer