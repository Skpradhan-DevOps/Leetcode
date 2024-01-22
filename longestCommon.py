class Solution:
    def longestCommonPrefix(self, strs):
        x=strs[0]
        l=len(strs)
        lx=len(x)
        for i in range(1,l):
            while x!="":
                if x in strs[i]:
                    flag=1
                else:
                    flag=0
                l=l-1
                x=x[:l]
                    
