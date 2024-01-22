a=0
while a<10:
   print(a)
   a=a+1

print('=========================')

for b in range(2,11,2):
    print(b, end=" ")


print("\n",'=========================')

l1=[10,15,20,25]
l2=["Srikant","Jenny","ADV",25]
for i in l1:
   print(i)
for j in l2:
   print(j)
l1[1]=50
print("\n","after change in list:")
for i in l1:
   print(i)

print("\n",'=========================')

t=(2,5,8,10)
for i in t:
   print(i)

print("\n",'=========================')

s={2,5,8,10, "Srikant"}
for i in s:
   print(i)