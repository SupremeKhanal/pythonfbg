#python collection
#List
#-indexing
# -Multiple and duplicate data
# -Mutable data type

# -ordered
a=list()
a=[1,2,3,4,5,6,7,8,9,0]
b=["Apple","Ball","Cat","Dog","Fish"]
print(type(a))
print(type(b))
print(a)
print(b)

print(a[0])
print(a [0:5])
print(b[0:5])
print(b[0:5:2])

a=[1,2,3,4,5,6,7,8,9,0]
b=["Apple","Ball","Cat","Dog","Fish"]
c=a+b
print(c)
print(b*2)
#append() insert() extend
b=["apple","ball","cat","dog"]
b.append("ball")
print (b)
#create a list
a=[]
n=int(input("Enter n= "))
for i in range(n):
    x=int(input("Enter x ="))
    a.append(x)

print (a)
print("Min value=",min(a))
print("Max value =",max(a))
print("sum value=",sum(a))
a.sort()
print(a)
a.reverse()
print(a)
#
a=["ball","kera","fish"]
a.sort()
print(a)
#insert()#extend
a=["ball","Xray","Yak","aple","Banana"]
b=[1,2,3]
a.insert(1,"Bat")
print(a)
a.extend(b)
print(a)
#edit
a=["Ball","Xray","Yak"]
a[0]="ball"
print(a)
#
a=["ball","xray","yak","apple","banana"]
a[0:2]=["Ball","Xray"]
print (a)
#to remove
#del remove() pop()
a=["Ball","Xray","Yak","Apple","Banana"]
del a[0]
print(a)
del a[0:2]
print (a)
a.remove("Ball")
#pop()
a=['ball','Xray','yak','appple','banana']
b=a.pop(0)
print(a)
print(b)
#loop in list
a=["Ball","Xray","Yak","Apple","Banana"]
for i in a:
    print(i)
print(len(a))
#while loop in list
a=["Ball","Xray","Yak","Apple","Banana"]
i=0
l=len(a)
while i<l:
    print(a[i])
    i=i+1





# Tuple
#dict
#Set
