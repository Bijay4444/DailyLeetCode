"""58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
consisting of non-space characters only.
"""
s = "Hello World"

string = s.split()
last_word = string[-1]

count = 0
for i in last_word:
    print(i)
    count += 1
    
print(count)
