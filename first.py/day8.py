
a=" Hello"
b=" world"
c=a+b
print(c)
#
a="Hello world\n"
print (a*2)
#
a="Hello world"
for i in a:
    print(i,end="")

#string slicing
a="HELLO World"
print(a[0])
print(a[0:4])
print(a[0:11:2])
#
a="Hello World"
print (a[-1])
print (a[-1:-12:-1])
print(a[::-1])
#
a="Hello world "
l=len(a)
for i in range(l):
    print(a[i],end="")
#
i=0
a="Hello WORLD"
l=len(a)
while i<l:
    print(a[i],end="")
    i=i+1
#
name=input ("enter the string ")
b=""
for i in range(len(a),0,-1):
    b=b+i

print(b)