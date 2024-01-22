import random
class Solution:
    def kth_largest_in_an_array(self,numbers, k):
        
 
    # Write your code here.
        def helper(numbers, start, end, index):
                #base case
                if start==end:
                    return
                
                #recursive internal node
                #Lomuto's Partitioning
                #pivot_index=random.randint(0,len(numbers)-1)
                pivot_index=(len(numbers)-1)//2
                #print(pivot_index)
                numbers[pivot_index], numbers[start] = numbers[start], numbers[pivot_index]
                
                orange= start
                for green in range(start+1, end+1):
                    if numbers[green] <= numbers[start]:
                        orange+=1
                        numbers[green], numbers[orange]=numbers[orange],numbers[green] 
                        
                numbers[start], numbers[orange] = numbers[orange], numbers[start]
                
                #lucky case
                if orange == index:
                    return
                elif index < orange:
                    helper(numbers, start, orange-1, index)
                        
                else:
                    helper(numbers, orange+1, end, index)
                
        helper(numbers, 0, len(numbers)-1, len(numbers)-k)
                        
        return numbers[len(numbers)-k]

numbers=[5, 1, 10, 3, 2]
k=2
sol=Solution()
print(sol.kth_largest_in_an_array(numbers, k))
