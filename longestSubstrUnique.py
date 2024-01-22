def longest(string1):
    res=dict()
    for i in range(len(string1)):
        for j in range(i+1,len(string1)):
            if string1[i]==string1[j]:
                res[(string1[i:j])]=[len(string1[i:j])]
                break

    return max(res,key=res.get),max(res.values())
    #return res

s="bbbbb"
print(longest(s))
