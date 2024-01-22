class Solution:
    def generate_all_combinations(arr, target):
        res=[]
        def helper(arr, i, slate):
            #backtracking:
            if sum(slate) > target:
                return
            elif sum(slate) == target:
                res.append(slate[:])
                return res
            #recursive Case: Internal node
            count = 0
            for index in range(i, len(arr)):
                if arr[index] != arr[i]:
                    break
                count+=1
                
            #exclude
            helper(arr, i+count, slate)
            
            #include
            for c in range(1, count+1):
                slate.append(arr[i])
                helper(arr, i+count, slate)
                slate.pop()

        return res

sol=Solution()
arr=[1, 2, 3]
target=3
print(sol.generate_all_combinations(arr, target)
