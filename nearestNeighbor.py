#from scipy.spatial import distance
from math import dist
class Solution:
    
    def nearest_neighbours(self,p_x, p_y, k, n_points):
        """
        Args:
         p_x(int32)
         p_y(int32)
         k(int32)
         n_points(list_list_int32)
        Returns:
         list_list_int32
        """
        # Write your code here.
        distance={}
        res=()
        print(type(res))
        p = (p_x, p_y)
        for n in n_points:
            d = dist(p, n)
            distance[tuple(n)]=d
            
        dict(sorted(distance.items(), key=lambda item: item[1]))
        
        for i in range(1, k+1):
            #res.append(distance.keys())
            print(distance.keys())
            
        return res

p_x = 1
p_y = 1
k = 1,
n_points = [[0, 0],[1, 0]]

sol=Solution()
print(sol.nearest_neighbours(p_x, p_y, k, n_points))
