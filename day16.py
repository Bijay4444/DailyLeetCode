"""66. Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is 
the ith digit of the integer. The digits are ordered from most significant to least significant 
in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""
def plusone(digits):
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += 1
        
        if digits[i] == 10:
            digits[i] = 0
        else:
            return digits
        
    return [1] + digits

print(plusone(digits=[9,9,0]))