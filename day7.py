"""
13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        rep = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        
        for i in range(len(s)):
            if i < len(s) -1 and rep[s[i]] < rep[s[i+1]]:
                total -= rep[s[i]]
            else:
                total += rep[s[i]]
                
        return total