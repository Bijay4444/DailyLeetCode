"""66. Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is 
the ith digit of the integer. The digits are ordered from most significant to least significant 
in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""
digits = [1, 2, 9]

# for i in digits:
    # if digits[i] <= 9:
    #     digits[-1] + 1
updated= digits[-1] + 1
digits.pop(-1)
digits.append(updated)
print(digits)

for i in digits:
    if i >= 9:
        digits.pop(-1)
        updated = 0
        digits.append(updated)
        print(digits)
        
        digits.pop(-2)
        updated = digits[-2]+ 1
        digits[-2] = updated
        print(digits)

print(digits)
        