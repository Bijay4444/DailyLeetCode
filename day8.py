"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        # zip(*strs) zips the strings together, producing tuples of corresponding characters
        for i, char_tuple in enumerate(zip(*strs)):
            # if all characters in char_tuple are not the same, return the prefix up to i
            if len(set(char_tuple)) > 1:
                return strs[0][:i]
        
        # If no mismatch found, return the entire first string (minimum length among all)
        return min(strs, key=len)
                
