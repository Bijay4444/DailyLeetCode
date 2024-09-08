"""
49. Group Anagrams

Given an array of strings strs, group the 
anagrams together. You can return the answer in any order.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}
        
        for s in strs:
            # Create a character frequency tuple
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Convert the list to a tuple to use as a key
            key = tuple(count)
            
            if key not in anagram_map:
                anagram_map[key] = []
            
            anagram_map[key].append(s)
        
        return list(anagram_map.values())
