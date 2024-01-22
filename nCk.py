class Solution:
    def find_combinations(self,n, k):
        """
        Args:
         n(int32)
         k(int32)
        Returns:
         list_list_int32
        """
        # Write your code here.
        res=[]
        def helper(n, k, i, slate):
            if len(slate)==k:
                res.append(slate[:])
                return

            for a in range(i,n+1):
                slate.append(a)
                helper(n,k,a+1,slate)
                slate.pop()
            
            
            
        helper(n,k,1,[])    
        return res

n=5
k=2
sol=Solution()
print(sol.find_combinations(n, k))
