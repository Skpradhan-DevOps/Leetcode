class Solution:
    def maxArea(self,height):
        l=len(height)
        #print(l)
        m=1
        out=0
        mArea=[]


        for i in range(l):
            for j in range(1,l):
                x=min(height[i],height[j])
                area=x*abs(j-i)
                out=max(area,out)
                #mArea.append(area)
        #return(max(mArea))
              

        #for i in mArea:
            #if i>m:
                #m=i
        #print(m)
        return out

height=[0,2]
sol=Solution()
print(sol.maxArea(height))               
    
                    
