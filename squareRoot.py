import math
x=int(input("Enter a number:"))
print(math.sqrt(x))

print("======================================================")

x=int(input("Enter a number:"))

#l=[2,3,5,7,11]
l=[]

#start=1
end=100

for i in range(2, end+1):
    #if i > 1:
        for j in range(2, i):
            if(i % j == 0):
                break
        else:
            l.append(i)

print(l)


#k=0
l1=[]

for i in l:
    while x%i==0:
        x=x/i
        #k=k+1
        l1.append(i)
    #c.append(k)
print(l1)

#c = {i:int(l1.count(i)/2) for i in l1}
#print(c)

finalist = {i**int(l1.count(i)/2) for i in l1}
print(finalist)

#c1=[]
#for j in c:
 #   j=j/2
  #  c1.append(j)

#l2=[]
#for i in l1:
 #   if i not in l2:
  #      l2.append(i)

#r1=range(len(l2))
#n=0
#sq=1
#finalist=[]
#for n in r1:
  # sq=l2[n]*c1[n]
  # finalist.append(sq)

final=1
for i in finalist:
    final=final*i

print("square root of the number is:", final)
   
       

      
      
