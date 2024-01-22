class Solution:
    def arrayInt(self,arr):
        res=[]

        def helper(arr,i,slate):

        
            if i==len(arr):
                res.append(slate[:])
                return res

            for a in range(i,len(arr)):
                arr[a],arr[i]=arr[i],arr[a]
                slate.append(arr[i])
                helper(arr,i+1,slate)
                slate.pop()
                arr[i],arr[a]=arr[a],arr[i]

        helper(arr,0,[])
        print(res)

sol=Solution()
sol.arrayInt([1, 2, 2])

            
