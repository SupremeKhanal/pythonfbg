#control statements

#pass
for i in range (5):
    pass
#continue
n=10
for i in range(n):
    if i==5:
        continue
    print(i,end=" ")
# break
a="Hello world. I am Python"
for i in a:
    if i=="I":
        break
    print(i,end="")
n=10
for i in range(n):
    print(i)
    if i==5:
        break
#________________________________________________________________________________________
a="Hello world .I am Python"
for i in (a):
    if i!="." and i!="o":
        print (i,end="")

a="Hello World"
for i in a:
    print(i,"\nHello World")

#for loop in string
a="Hello World"
for i in a:
    print(i,end="")# to print horizontally

info=""
n=int(input("\nhow many items u want to purchase?="))
for i in range(n):
    name=input("enter product name=")
    price=int(input("enter the price"))
    quantity=int(input("enter the quantity"))
    total=price*quantity
    info =info +name+" "+str(price)+" "+str(quantity)+" "+str(total)+"\n"


print("\n\tBilling Details:")
print("\t{:<15} | {:<10} | {:<10} | {:<10}".format("Item Name", "Price", "Quantity", "Total"))
print("\t"*info)