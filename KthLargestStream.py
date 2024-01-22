import heapq
class Solution:
    
    def kth_largest(self,k, initial_stream, append_stream):
        """
        Args:
         k(int32)
         initial_stream(list_int32)
         append_stream(list_int32)
        Returns:
         list_int32
        """
        # Write your code here.
        res=[]
        heapq.heapify(initial_stream)
        for num in append_stream:
            heapq.heappush(initial_stream, num)
            temp=initial_stream
            n = len(temp)
            '''for i in range(n-k+1):
                klargest=heapq.heappop(initial_stream)
                temp.append(klargest)
            res.append(klargest)
            for a in temp:
                heapq.heappush(initial_stream,a)'''
                
            while n > k:
               heapq.heappop(temp)
               n-=1
            res.append(temp[0])   
                
        return res
k=2
initial_stream=[4,6]
append_stream=[5, 2, 20]
sol=Solution()
print(sol.kth_largest(k, initial_stream, append_stream))
