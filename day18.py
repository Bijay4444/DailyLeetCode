"""Given a non-negative integer x, return the square root of 
x rounded down to the nearest integer. The returned integer 
should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x==1:
            return x
        
        start = 1
        end = x//2
        
        while (start <= end):
            mid = (start+end) // 2
            
            if(mid*mid == x):
                return mid
            
            if(mid * mid < x):
                start = mid + 1
                ans = mid 
            else:
                end = mid - 1
                
        return ans
           