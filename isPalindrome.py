class Solution:
    def isPalindrome(self,x):
        x=str(x)
        if x==x[::-1]:
            return True
        else:
            return False

n=int(input())
sol=Solution()
print(str(sol.isPalindrome(n)).lower())
      
