"""
49. Group Anagrams

Given an array of strings strs, group the 
anagrams together. You can return the answer in any order.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagaram_map = {}
        
        for s in strs:
            sorted_str = ''.join(sorted(s))
            
            if sorted_str not in anagaram_map:
                anagaram_map[sorted_str] = []
                
            anagaram_map[sorted_str].append(s)
        
        return list(anagaram_map.values())