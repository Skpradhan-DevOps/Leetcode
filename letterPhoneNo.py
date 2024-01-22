class Solution:
    def get_words_from_phone_number(self,phone_number):
    # Write your code here.
        res=[]
        noToChar = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    
        def helper(phone_number, i, slate):
            if i == len(phone_number):
                res.append(slate)
                return res
            
            #recursive
            for d in phone_number:
                if d == "1":
                    phone_number=phone_number[:phone_number.index(d)] + phone_number[phone_number.index(d)+1:]
            for c in noToChar[phone_number[i]]:
                #if phone_number[i] == "1":
                #    i +=1
                #while c != "":
                helper(phone_number, i+1, slate + c)
                    
                
            
        helper(phone_number, 0, "")
        return res,len(res)

sol=Solution()
print(sol.get_words_from_phone_number("7979"))
