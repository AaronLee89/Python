#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
class Solution(object):
    def match(self,s1,s2):
        if s1 == '(' and s2 ==')':
            return True
        if s1 == '[' and s2 ==']':
            return True
        if s1 == '{' and s2 =='}':
            return True
        return False
    def isValid(self, s):
        ans = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                ans.append(i)
            if i == ')' or i == ']' or i == '}':
                if len(ans) == 0:
                    return False
                tmp = ans.pop()
                if not self.match(tmp,i):
                    return False
        if len(ans) == 0:
            return True
        return False