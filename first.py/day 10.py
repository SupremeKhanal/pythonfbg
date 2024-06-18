#nested list(list inside list)
l=[[1,2,3],[4,5,6],[7,8,9]]
print (l[0])
print(l[1])
print(l[1][0])


i=[["ram",34,"Kathmandu"],["shyam",67,"bhaktapur"],["Hari",15,"Lalitpur"]]
print(i)
#WAP to create list inside list
info=[]
n=int(input("enter n="))
for i in range(n):
    name=input("enter name= ")
    age=int(input("enter your age= "))
    add=input("Enter add =")
    info.append([name,age,add])

for inf in info:
    print(inf[0],inf[1],inf[2])
# to edit in lists
l=[['ram',25,'Kathmandu'],['shyam',56,'bhaktapur']]
l[0][0]='ram prasad'
print(l)
#delete
del l[0]
print (l)
#search
i=[["shyam",67,"bhaktapur"],["hari",15,"Lalitpur"],["ram",34,"Kathmandu"]]
name=input("enter the name u want to search")
for l in i:
    if name.lower() in l:
        print (l)
#
a=["ram","shyam","hari","ram"]
if "ram" in a:
    print("Yes",a.count("ram"),"ram")
#
l=[["shyam",67,"bhaktapur"],["hari",15,"Lalitpur"],["ram",34,"Kathmandu"]]
name=input("enter name= ")
for i in l:
    if name in i:
        print(i[0],"is",i[1])
#
l=[["shyam",67,"bhaktapur"],["hari",15,"Lalitpur"],["ram",34,"Kathmandu"]]

name=input("name")
for  i in l:
    if name.lower() in i[0].lower():
        print(i)
#WAP to remove multiple data from list
l=["Apple","Ball","Cat","Fish","Apple"]




#WAP to find index of duplicate data from list




