"""
def hello():
    print("hello")
hi = hello
hi()
hello()

import math
pi = 3.14
print(round(pi))
print(math.ceil(pi))
print(abs(pi))
print(math.sqrt(pi))
print(pow(pi,6))

x = 1
y = 2
z = 3
print(max(x,y,z))
Germain = "Safari"
first_name = Germain 
print(first_name)
name = "bro code"
print()
"""

def lengthOfLongestSubstring(s):
        
        """
        :type s: str
        :rtype: int
        """
        string = []
        for i in range(len(s)):
            if s[i] in string:
                break
        else:
            string.append(s[i])
        return string
s = "abcabcbb"
res = lengthOfLongestSubstring(s)
print(res)
