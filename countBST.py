def countBST(n):

    if n<=1:
        return 1
    count=0

    for i in range(n):
        count += countBST(i)*countBST(n-i-1)

    return count

for i in range(10):
    print (countBST(i),end=" ")
