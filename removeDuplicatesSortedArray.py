a=[]
n=int(input("Enter a number for array list:"))

for x in range(0,n):
    b=int(input())
    a.append(b)
print(a)

d=[]
for x in a:
    if x not in d:
        d.append(x)
print(d)
d.sort()
print(d)
l=len(d)
for x in range(l,n):
    d.append("_")

print(d)
translation = {39: None}
print(str(d).translate(translation))

    
      
