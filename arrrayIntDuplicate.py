class Solution:
    def arrayInt(self,arr):
        res=[]

        def helper(arr,i,slate):

        
            if i==len(arr):
                res.append(slate[:])
                return res


            for pos in range(i,len(arr)):
                hmap=set()
                if arr[pos] in hmap:
                    continue
                hmap.add(arr[pos])
                if (i > 0 and arr[i] == arr[i - 1] and hmap[i - 1]==True):
		    continue
                arr[pos],arr[i]=arr[i],arr[pos]
                slate.append(arr[pos])
                helper(arr,i+1,slate)
                slate.pop()
                arr[pos],arr[i]=arr[i],arr[pos]

        helper(arr,0,[])
        print(res)

sol=Solution()
sol.arrayInt([1, 2, 2])

def get_permutations(arr):

    path = []

    res = []


    def helper(arr,path,res):

        if not arr:

            res.append(path)


        for i in range(len(arr)):

            if i>0 and arr[i-1] == arr[i]:

                continue

        helper(arr[:i]+arr[i+1:],path+[arr[i]],res)
    

        helper(sorted(arr),path,res)

    return res


            
