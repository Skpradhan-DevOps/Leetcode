class Solution:
    def letterCombinations(self, digits):
        number=['2','3','4','5','6','7','8','9']
        letter=["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        if digits=="":
            return []
        digitList=list(digits)
        print(digitList)
        l1=len(digits)
        letterList=[]
        for i in digitList:
            a=number.index(i)
            b=letter[a]
            letterList.append(b)
        
        l2=len(letterList)
        temp=letterList[0]
        for i in range(1,l2):
            temp=self.finalCombo(temp,letterList[i])
            
            
            
        return list(temp)
    
    
    def finalCombo(self,temp,S2):
        letterPhone=[]
        for i in temp:
            for j in S2:
                a=i+j
                letterPhone.append(a)
        return letterPhone
        
                
digits="23"
sol=Solution()
print(sol.letterCombinations(digits))
        
