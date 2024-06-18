#Tuples
#-indexing
#-Ordered
#-Multiple and Duplicate
#-Immutable

# to define a tuple
#t=tuple() Unchangable data type where the data cannot be edited /append/insert/extend/sort
t=(1,2,3,4,5,6,7,8,9)
print(type(t))
#
a=(1,2,3,4,5)
b=(6,7,8,9)
c=a+b
print(c)
#
a=("Apple","Banana","Cat","Dog","Fish")
print(a[0])
print(a[0:3])
#
t=(1,2)
print (type(t))
#
t=tuple()
n=int(input("enter n= "))
for i in range(n):
    x=int(input("Enter the value x= "))
    t=t+(x,) # To concat
print(t)

#set()
# -No indexing
# -Unordered
# -Multiple data but no Duplicate
# -Mutable
#Keeps the value unique(not repeated)
s=set()
s={"Apple","Banana","Mango","Cat ","Monkey"} #-It doesnot supports Duplicate datas
# The printed value can come in random order
print(s)
for i in s:
    print(i)
#
s={"Apple","Banana","Cat","Banana"}
print(s)#output comes without any Dupes
#
s=set()
s.add("Apple")
s.add("Ball")
s.add("Cat")
#to put multiple at once
s={'Ball','Cat','Apple'}
a={1,2,3,4}
s.update(a)
#
s={'Ball','Cat','Apple'}
s.remove("Ball")
print(s)
# To find intersection ( Same as math concept)

a={1,3,4,5,6,9}
b={0,2,4,5,9}
c=a.intersection(b)
print(c)
#Union
a={1,3,4,5,6,9}
b={0,2,4,5,9}
d=a.union(b)
print(d)
#
a={1,3,4,5,6,9}
b={0,2,4,5,9}
print(b-a)
print(a-b)
#
U={0,1,2,3,4,5,6,7,8,9}
a={1,3,5,7,8,9}
b={2,3,5,8}
c=U-a.union(b)
print(c)
#No set inside set
#NO! list inside set
#But Tuples can be inside Set
#
s={(1,2),(3,4)}
print(s)