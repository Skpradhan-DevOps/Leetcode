a=10.5
b=20
sum=a+b
print("sum is :", sum)
print(type(a))
print(id(a))

c=5
d=5
print("=======================================")
print(id(c))
print(id(d))
print("=======================================")

import keyword
print(keyword.kwlist)

print("=======================================")

s="Srikant"
print(s[-2:])
print(s[:-2])

print("=======================================")

e=10+5j
f=10+5j
print(e is f)
print(id(e))
print(id(f))

print("=======================================")
x =[10,255]
b = bytearray(x)

print("=======================================")

a=10
print(a)
a=20
print(a)
