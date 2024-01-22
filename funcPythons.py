a=10
print(type(a))
a="Srikant"
print(type(a))
a=[2,5,6]
print(type(a))
a=(5,6,8)
print(type(a))
a={5,6,8}
print(type(a))
a=True
print(type(a))
a=1.6
print(type(a))

print("==================================")

b=10
c=10
print(id(b))
print(id(c))

print("====================================")

a=10
b=0o102
c=0X1fa
d=0B111
print(a)
print(b)
print(c)
print(d)

print("====================================")

x=oct(10)
y=bin(15)
z=hex(100)
a=oct(0x123)
print(x,y,z,a)

print("++++++++++++++++++++++++++++++++++++++")

f=1.06986
print(type(f))
f=1.2e3
print(f)

print("====================================")

a=3+5j
b=0b11+1.5j
c=a+b
print(a,b,c)
print(c.real,c.imag)

print("====================================")

a=True
b=False
c=a+b
print(type(a))
print(c)
d=5
e=8
print(d>e)

print("====================================")

s="Jenny"
t='Srikant'
print(t,"loves",s)
d= """Jenny
 Srikant"""
print(d)
e="Srikant's lapi"
f='Mac is "excellent" OS'
print(e,"\n", f)
print(e,f)
print(s[0],s[-1])
print(len(e))

print("====================================")

def print_even(test_list) :
    for i in test_list:
        if i % 2 == 0:
            yield i
 
# initializing list
test_list = [1, 4, 5, 6, 7]
 
# printing initial list
print ("The original list is : " +  str(test_list))
 
# printing even numbers
print ("The even numbers in list are : ", end = "->")
for j in print_even(test_list):
    print (j, end = ",")



