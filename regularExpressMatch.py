import re
class Solution:
    def isMatch(self,s,p):
        #return s in re.findall(p,s)
        return re.fullmatch(p,s)
        #print(x)

s=str(input("Enter a string:"))
p=input("Enter a pattern:")
sol=Solution()
print(sol.isMatch(s,p))
