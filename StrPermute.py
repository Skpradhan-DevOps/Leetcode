class Solution:
    
    def permute(self,s):
        result=[]
        

        def helper(s, i, Slate):
            #base condition
            if i==len(s):
                result.append(Slate[:])
                #print(result)
                return result

            #intenal recursive function
            if s[i].isdigit():
                Slate.append(s[i])
                helper(s,i+1,Slate)
                Slate.pop()

            if s[i].isalpha():
                Slate.append(s[i].upper())
                helper(s,i+1,Slate)
                Slate.pop()
                Slate.append(s[i].lower())
                helper(s,i+1,Slate)
                Slate.pop()
            
    
        helper(s,0,[])
        return result

sol=Solution()
print(sol.permute("a1b2"))
