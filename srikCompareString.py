class Solution:
    def compareString(self,S1,S2):
        maxS1=[]
        l1=len(S1)
        compS1S2=[]
        comp=""
        for i in range(l1):
            for l in range(i+1,l1+1):
                subst=S1[i:l]
                maxS1.append(subst)

        for i in maxS1:
            if i in S2:
                compS1S2.append(i)
        if len(compS1S2)==0:
            return comp
        else:
            return max(compS1S2, key=len)

        

    def longestCommonPrefix(self,strs):
        l2=len(strs)
        temp=strs[0]
        for i in range(l2):
            longCom=self.compareString(temp,strs[i])
            temp=longCom
        return temp
            
                
            

strs = ["dog","racecar","car"]
sol=Solution()
print(sol.longestCommonPrefix(strs))
