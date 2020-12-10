"""
json = "{'text': {'text': [ 'My hobby is fishing, reading and dancing']}}"
words = … # continue your code from here

Suppose the above codes are at the start of a python program. Write the code that follows to achieve the following:

a)	Extracted all the individual words from the json structure before assign them to the words variable. 
b)	Print the number of words in the string json
c)	Print "My hobby is reading and dancing" by appending the words variable. Note that you must remove all the punctuations within the variables.  
"""

import re

json = "{'text': {'text': [ 'My hobby is fishing, reading and dancing']}}"

words=re.findall(r'\w+',json)
print(words)                           # Part a)

num_words = len(words)
print(num_words)                       # Part b)

words.remove("text")
words.remove("text")
words.remove("fishing")
append_words=""
for i in words:
 append_words=append_words+str(i)+" "
print(append_words)                    # Part c)
