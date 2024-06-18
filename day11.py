#dictionary
#indexing
#multiple and duplicate values
#oredered
#mutable
#d={<key>:<value>,<key>:<value>}
d={'a':'Apple','b':'Ball'}
print (d)
print(type(d))
print(d['a'])
#dict  (to make a dictionary)
d={}
d['a']="Apple"
d['b']="Ball"
d['c']="Cat"
print(d)
#WAP to creat a dict using name and phone
d={}
n=int(input("Enter n="))
for i in range (n):
    name=input("enter name= ")
    phone=input("enter phone= ")
    d[name]=phone
    print(d)

for i in d: #to print keys
    print(i)
for i in d.values():# to print values
    print(i)
for i in d.items()# to print the entire dictionary
    print(i)
# in dictionary no + or -
# to edit
d={'Ram':'9849500777','Shyam':'9851061300'}
d['Ram']=9863483222
print (d)
# to delete
d={'Ram':'9849500777','Shyam':'9851061300'}
del d['Ram']
print(d)
#pop()
d={'Ram':'9849500777','Shyam':'9851061300'}
x=d.pop('Ram')
print(x)

#list inside dictionary
d={'Ram':[9812345678,9801234567],'Shyam':[9867322211,9812345687]}
print(d['Ram'])
print(d['Shyam'])

print(d['Ram'][0])

# to create a dict with lists
d={}
n=int(input("Enter n="))
for i in range (n):
    name=input("enter name= ")
    ntc=input("enter ntc no. = ")
    ncell=input("Enter ncell no.=")
    d[name]=[ntc,ncell]
print(d)
#edit or delete
d={'Ram':[9812345678,9801234567],'Shyam':[9867322211,9812345687]}
del d['Ram'][1]
print (d)
d={'Ram':[9812345678,9801234567],'Shyam':[9867322211,9812345687]}
d['Ram'][0]=9869696969
print (d)

#relevant format for dictionary
d={'name':['Ram','Shyam'],
    'age':[34,56],
    'add':['Kathmandu','Bhakatapur']}
print (d)
# to manike a table using dcitionary by asking from user
d={'name':[],'age':[],'add':[]}
n=int(input("enter n = "))
for i in range(n):
    name=input("enter name = ")
    age=int(input("enter age = "))
    add=input("enter add= ")
    d['name'].append(name)
    d['age'].append(age)
    d['add'].append(add)
print(d)
#to print the details
print(d['name'][0])
print(d['age'[0]])
print(d['add'[0]])
# to del the details
del d['name'][0]
del d['age'[0]
del d['add'[0]]

#dictionary inside list
l=[{'name':'shyam','age':'23','add':'Jhapa'},{'name':'Hari','age':'15','add':'palpa'}]
print(l[0])

#dictionary inside dictionary
l={1:{'name':'shyam','age':'23','add':'Jhapa'},2:{'name':'Hari','age':'15','add':'palpa'}}
# example of dictionary inside a list
l=[]
n=int(input("enter n= "))
for i in range(n):
    name=input("enter name = ")
    age=int(input("enter age = "))
    add=input("enter add= ")
    d={'name':name,'age':age,'add':add}
    l.append(d)
print(l)