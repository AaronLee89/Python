# Reverse digits of an integer.
# Example1: x = 123, return 321
# Example2: x = -123, return -321
class Solution(object):
    def reverse(self, x):
        max = 2147483648  
        min = -2147483648
        if(x == 0):
            return 0
        ret = 0
        flag = 1
        if x < 0:
            flag = -1
            x *= -1
        while(x!=0):
            ret = ret*10+x%10
            x = x/10
        if(ret > max or ret < min):
            return 0
        return ret*flag
