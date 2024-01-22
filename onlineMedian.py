import heapq
class Solution:
    def online_median(self,stream):
        """
        Args:
         stream(list_int32)
        Returns:
         list_int32
        """
        # Write your code here.
        maxheap=[]
        minheap=[]
        res=[]
        heapq.heapify(maxheap)
        heapq.heapify(minheap)
        median=0.0
        maxroot=0
        minroot=0
        for num in stream:
            if num > median:
                heapq.heappush(minheap, num)
                print(len(minheap) - len(maxheap))
                if len(minheap) - len(maxheap) == 2:
                    heapq.heappop(minheap)
                    heapq.heappush(maxheap,-num)
            else:
                heapq.heappush(maxheap, num)
                if len(maxheap) - len(minheap) == 2:
                    heapq.heappop(maxheap)
                    heapq.heappush(minheap, -num)
            print(maxheap, minheap)        
            if minheap:
                minroot=heapq.heappop(minheap)
            if maxheap:
                maxroot=heapq.heappop(maxheap)
            print(maxheap, minheap)
            if minheap != 0:
                heapq.heappush(minheap, minroot)
            
            if maxroot != 0:
                heapq.heappush(maxheap, maxroot)
            print(maxheap, minheap)
            if len(minheap) == len(maxheap):
                print(maxheap, minheap)
                median= (minroot - maxroot)//2
            elif len(minheap) < len(maxheap):
                #print(maxheap, minheap)
                median = maxroot
            else:
                #print(maxheap, minheap)
                median = minroot
                
            #heapq.heappush(minheap, minroot)
            #heapq.heappush(maxheap, maxroot)
                
            res.append(median)
                
                
        return res

stream=[3, 8, 5, 2]
sol=Solution()
print(sol.online_median(stream))
