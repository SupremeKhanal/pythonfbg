def hello(to):
    print("Hello",to)


name=input("enter your name? ")
hello(name)
#
def hello(to="World"):
    print("Hello",to)

hello()
name=input("enter your name? ")
hello(name)
#
def main():
    name=input("Enter your name= ")
    hello(name)

def hello(to="world"):
    print("Hello",to)

main()
#
score=int(input("Score: "))
if score >=90 and score <=100:
    print("Grade:A")
elif score>=80 and score<90:
    print("Grade:B")
elif score >=70 and score <80:
    print("Grade :C")
elif score >=60 and score <70:
    print("Grade:D")
else:
    print("Grade:F")

#Match
name = input("Enter your name = ")

match name:
    case "Harry":
        print("bottal")
    case "Ram":
        print("RAMUJI")
    case _:
        print("Name not recognized")



#(
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Enter N= "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()
#

students=["Herimone","Harry","Ron"]

for i in range(len(students)):
    print(i+1,students[i])
#

students=["Herimone","Harry","Ron","Draco"]
houses=["Gryfindor","Gryfindor","Gryfindor","Slytherin"]
#same thing using dictionary

students={"Herimone":"Gryffindor","Harry":"Gryffindor",
          "Ron":"Gryffindor"}






