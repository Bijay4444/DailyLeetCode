"""58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
consisting of non-space characters only.
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.split()
        count = 0
        last_word = string[-1]

        for i in last_word:
            count += 1

        return count