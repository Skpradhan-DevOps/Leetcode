# Python3 Program to implement
# the above approach

# Function to fill the vector curr
# while maintaining the indices visited
# in the array num
def backtrack():
	global ans, curr, visited, nums
	
	# If current permutation is complete
	# print(ans)
	if (len(curr) == len(nums)):
		print(*curr)

	# Traverse the input vector
	for i in range(len(nums)):

		# If index is already visited
		if (visited[i]):
			continue

		# If the number is duplicate
		if (i > 0 and nums[i] == nums[i - 1] and visited[i - 1]==True):
			continue

		# Set visited[i] flag as true
		visited[i] = True

		# Push nums[i] to current vector
		curr.append(nums[i])

		# Recursive function call
		backtrack()

		# Backtrack to the previous
		# state by unsetting visited[i]
		visited[i] = False

		# Pop nums[i] and place at
		# the back of the vector
		del curr[-1]

# Function to pre-process the vector num
def permuteDuplicates(nums):
	global ans, visited, curr
	nums = sorted(nums)

	# Find the distinct permutations of num
	backtrack()
	return ans

# Function call to print all distinct
# permutations of the vector nums
def getDistinctPermutations(nums):
	global ans, curr, visited
	
	# Find the distinct permutations
	ans = permuteDuplicates(nums)

# Driver Code
if __name__ == '__main__':
	visited = [False]*(5)
	ans,curr = [], []
	nums = [1, 2, 2]

	# Function call to print
	# all distinct permutations
	getDistinctPermutations(nums)

	# This code is contributed by mohit kumar 29.
