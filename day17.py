"""
Given two binary strings a and b, return their sum as a binary string.
"""
a = "1010"
b = "1011"

sum_val = int(a, 2) + int(b, 2)

print(bin(sum_val)[2:])
            