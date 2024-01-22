class Solution:
    def isValid(self, s):
        temp = []
        opener = ["[", "(", "{"]
        for val in s:
            if val in opener:
                temp.append(val)
                print(temp)
            elif temp:
                cur = temp.pop()
                print(cur)
                if cur:
                    if val == ")" and cur !="(": return False
                    elif val == "]" and cur !="[": return False
                    elif val == "}" and cur !="{": return False
            else: return False
                
        if temp:
            return False
        else:
            return True

s="({})"
sol=Solution()
print(sol.isValid(s))
