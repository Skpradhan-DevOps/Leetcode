class Solution:
    
    def generate_all_expressions(self,s, target):
        """
        Args:
         s(str)
         target(int64)
        Returns:
         list_str
        """
        # Write your code here.
        n=len(s)
        ans=[]
        
        def dfs(i, total, prev_add, slate):
            if i == n and total == target:
                ans.append(slate)
                return ans
            
            for j in range(i+1, n+1):
                a = s[i:j]
                d = int(a)
                
                # to resolve "00" scenario
                if s[i] == '0' and a != '0':
                    continue
                
                if not slate:
                    dfs(j, d, d, a)
                else:
                    #+ condition
                    dfs(j, total + d, d, slate + '+' + a)
                    dfs(j, total + d, d, slate+a)
                    # * condiation
                    dfs(j, total - prev_add + prev_add * d, prev_add*d, slate + '*' + a)
                    
        dfs(0, 0, 0, "")
        return ans

s="202"
target=4
sol=Solution()
print(sol.generate_all_expressions(s, target))

