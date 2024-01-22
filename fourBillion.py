class Solution:    
    def find_integer(self,arr):
        """
        Args:
         arr(list_int64)
        Returns:
         int64
        """
        # Write your code here.
        def mergeSort(arr):
            if len(arr) <= 200000 and len(arr) >= 1:
                r = len(arr)//2
                L = arr[:r]
                M = arr[r:]
                
                mergeSort(L)
                mergeSort(M)
                
                i=j=k=0
                
                while i < len(L) and j < len(M):
                    if L[i] <= M[j]:
                        arr[k] = L[i]
                        i+=1
                    else:
                        arr[k] = M[j]
                        j+=1
                    k += 1
                    if (arr[k+1] - arr[k]) > 1:
                        return
                    
                while i < len(L):
                    arr[k] = L[i]
                    i += 1
                    k += 1
                    if (arr[k+1] - arr[k]) > 1:
                        return
                        
                while j < len(M):
                    arr[k] = M[j]
                    j += 1
                    k += 1
                    if (arr[k+1] - arr[k]) > 1:
                        return
                    
        mergeSort(arr)
        return arr[k+1]

arr=[0, 1, 2, 3]
sol= Solution()
sol.find_integer(arr)
