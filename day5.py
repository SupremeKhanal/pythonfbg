#loop statements
# for  loop
# while loop
 #range(5) output( 0,1,2,3,4)
#range (1,5)  output (1,2,3,4)
#range ( 1,5,2) output(1,3)
#range( 0,5,2) output (0,2,4)

#WAP to create a billing system
#name price quantity total

items = []
grandtotal = 0
x=int(input("how many items do u want to buy?="))
for i in range(x):
    name = input("Enter the item name (or type 'done' to finish without buying all): ")
    if name.lower() == 'done':
        break
    try:
        price = int(input("Enter the item price: "))
        quantity = int(input("Enter the item quantity: "))
    except ValueError:
        print("Invalid input. Please enter numeric values not string * .")
        continue
    total = price * quantity
    items.append((name, price, quantity, total))
    grandtotal = grandtotal+total
#chatak design
print("\n\tBilling Details:")
print("\t{:<15} | {:<10} | {:<10} | {:<10}".format("Item Name", "Price", "Quantity", "Total"))
print("-" * 69)
for item in items:
    print("\t{:<15} | {:<10} | {:<10} | {:<10}".format(item[0], item[1], item[2], item[3]))
#:< for left alignment| :> for right aligment {} <-- to store the input data(string ,boolen or numeric) in format type
# {:10} to add 10 space along with input data
#for item in items to find the item and print continuously until all the items are printed
print("-" * 69)#just a horizontal seperating line ('x')
print(" "*47+"Grand Total: {:<}".format(grandtotal))


#factorial
fac=1
n=int(input("enter n="))
for i in range(1,n+1):
    fac=fac*i
print(fac)





a=""
for i in range (3):
    name=input("enter name= ")
    age=int(input("enter age= "))
    add=input("enter add= ")
    a=a+name+" "+str(age)+" "+add+"\n"

print(a)
a =""
for i in range(5):
    x=input("enter x =")
    a=a+x+"\n"

    print(a)

sum = 0  # Initialize the sum variable
for i in range(5):
    y = int(input("enter the deposit value = "))
    sum = sum + y
print("deposited sum is ",sum)


for i in range (5):
     x=input("enter x=")             # to ask multiple values
     print("you entered ",x)

n=int(input("enter n="))
for i in range (1,11):
    print(n,"*",i,"=",n*i)


n=int(input("enter n="))
for i in range (1,11):
 print(n*i) # multiplication table


for i in range (0,5,2):
 print (i,"hello world")

for i in range(1,5):
    print (i,"hello world")




