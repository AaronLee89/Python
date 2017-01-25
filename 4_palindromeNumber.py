#Determine whether an integer is a palindrome. 
#Do this without extra space.
def isPalindrome(self,x):
    bef = x
    rev = 0
    if x < 0: x *= -1
    while(x!=0):
        rev = rev*10+x%10
        x = x/10

    if(rev != bef): 
    	return False 
    return True