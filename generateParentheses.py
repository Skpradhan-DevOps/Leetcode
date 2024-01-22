class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ["()"]
        
        
        ans = set()
        
        for s in self.generateParenthesis(n-1):
            ans.add("()" + s)
            ans.add(s+"()")
            ans.add("("+s+")")
            for i in range(len(s)):
                if s[i] == "(":
                    ans.add(s[:i+1] + "()" + s[i+1:])

        return list(ans)

n=2
sol=Solution()
print(sol.generateParenthesis(n))
