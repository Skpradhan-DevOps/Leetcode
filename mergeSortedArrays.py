def merge_one_into_another(first, second):
    """
    Args:
     first(list_int32)
     second(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    second=second[:len(first)]
    print(first)
    print(second)
    
    i=j=0
    out=[]
    
    while i<len(first) and j<len(second):
        if first[i]<second[j]:
            out.append(first[i])
            i=i+1
        else:
            out.append(second[j])
            j=j+1
    while j<len(second):
        out.append(second[j])
        j=j+1

# Print the array
    print("Sorted array is: ")
    for i in range(len(out)):
        print(out[i], end=" ")
        


# Driver program
if __name__ == '__main__':
    a = [1, 3, 5]
    b = [2, 4, 6, 0, 0, 0]

    merge_one_into_another(a, b)

