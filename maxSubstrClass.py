class Solution:
   def lengthOfLongestSubstring(self,P,N):
       S=dict()
       maxi=dict()
       l=1
       for i in range(N):
           freq = [False]*26
           s = ""
 
           for j in range(i,N):
               pos = ord(P[j]) - ord('a')
               if (freq[pos] == True):
                   break
 
               freq[pos] = True
               s += P[j]
               maxi.update({s:len(s)})
               if len(s) > l:
                   l=len(s)
       return l
       
Str = input("Enter a String:")
N = len(Str)
sol=Solution()
print(sol.lengthOfLongestSubstring(Str,N))
