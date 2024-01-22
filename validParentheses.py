class Solution:
    def isValid(self, s):
        if ("(" and ")" in s):
            if (s.startswith("(") and s.endswith(")")):
                return True
            else:
                return False
        if ("{" and "}" in s):
            if (s.startswith("{") and s.endswith("}")):
                return True
            else:
                return False
            
        
        if ("[" and "]" in s):
            if (s.startswith("[") and s.endswith("]")):
                return True
            else:
                return False

s="()[]{}"
sol=Solution()
print(sol.isValid(s))
