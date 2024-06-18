#Syntax for files
#file=open(<file_name>,<mode>)
#file.close()

#with open(<file name>,<mode>) as file:
    #<operations>

# mode
# create mode >c
# read mode >r
# write mode >w
# append mode>a

#To create a file
file=open('data.txt','x')
file.close()

#To read a file
file=open('data.txt','r')
x=file.read()
print(x)
file.close()
#

list_data=x.split('\n')
print(list_data)

#To write in data
file=open('data.txt','w')
file.write('Hello world')

file.close()
#To store the bill in a file

info=""
n=int(input("\nhow many items u want to purchase?="))
for i in range(n):
    name=input("enter product name=")
    price=int(input("enter the price"))
    quantity=int(input("enter the quantity"))
    total=price*quantity
    info=info+f"{name} {price} {quantity} {total}\n"
print(info)
#Writing on txt file
file=open('bill.txt','w')
file.write(info)
#to print data
file.close()
#
info=""
n=int(input("\nhow many items u want to purchase?="))
for i in range(n):
    name=input("enter product name=")
    price=int(input("enter the price"))
    quantity=int(input("enter the quantity"))
    total=price*quantity
    info=info+f"{name} ,{price}, {quantity}, {total}\n"
print(info)
#Writing on txt file
file=open('bill.csv','w')
file.write(info)
#to print data
file.close()


#
file=open('bill.csv','r')
data=file.read()
file.close()
l=data.split('\n')[0:-1]
print(data)
#
final_data=[]
for i in l:
    final_data.append(i.split(','))
print(final_data)


#
import csv
file=open('bill.csv','w')
x=csv.write(file)
x.writerows(final_data)
file.close()
#
