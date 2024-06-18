#good way
numbers=[5,2,5,2,2]
for x_count in numbers:
    output=''
    for count in range(x_count):
        output+='x'
    print(output)


#cheating way
numbers=[5,2,5,2,2]
for item in numbers:
    print('x'*item)
#
numbers= [1,9,10,3,5]
#
max=numbers[0]
for number in numbers:
    if number>max:
        max=number
print(max)
#2D use of list
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix:
    for item in row:
        print(item)
#
numbers=[5,2,1,7,4]
numbers.append(20)
print(numbers)
numbers.insert(0,10) #(here 0 is the index value and 10 is the item that we want to add)
#
numbers=[5,2,1,7,4]
print(numbers.index(7))
#
index=0
numbers=[5,2,1,7,1,4]
seen=[]
for number in numbers:
    if number not in seen:
        seen.append(number)
print(seen)
#
coordinates=(1,2,3)
x=coordinates[0]
y=coordinates[1]
z=coordinates[2]
#doing the same thing but shorter
#It's called unpacking the tuple
coordinates=(1,2,3)
x,y,z=coordinates
print(x*y*z)


#Dictionary
customer={
    "name":"John Smith",
    "age":30,
    "is_verified":True
}
print(customer["name"])
print(customer.get("Birthdata","Jan 1 1999"))
# To add new
customer["Behaviour"]="Excellent"
print(customer["Behaviour"])
#
phone=input("Phone: ")
Mapping={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five",
    "6":"Six",
    "7":"Seven",
    "8":"Eight",
    "9":"Nine",
    "0":"Zero"
}
output=""
for ch in phone:
    output+=Mapping.get(ch,"!")
print(output)
#
msg=input("--> ")
words=msg.split(' ')
emojis={
    ":)":"😊",
    ";9":"😘",
    ":(":"😒"
}
output=""
for word in words:
    output+=emojis.get(word,word)+" "
print(output)

#FUNCTION

def greet_user():
    print("Hi there!")              #When we run the function these 2 lines run
    print('Welcome Abroad')
#
#
print("Start")
greet_user()
print("Finish")

#Parameter ->How to add information to the function

def greet_user(nam,last_name):
    print(f"Hi there {nam} {last_name}!")              #When we run the function these 2 lines run
    print('Welcome Abroad')
#
#
print("Start")
greet_user("John","Smith")
print("Finish")

#
def greet_user(nam,last_name):
    print(f"Hi there {nam} {last_name}!")#When we run the function these 2 lines run
    print('Welcome Abroad')
#
#
print("Start")
greet_user(last_name="smith",nam="John")
#Keyword argument to improve readability
print("Finish")                              #Use postional argument at first then u can use keyword arguments  

#
def square(number):
    return number*number


print(square(3))
#
def emoji_converter(msg):
    words=msg.split(' ')
    emojis={
        ":)":"😊",
        ";9":"😘",
        ":(":"😒"
    }
    output=""
    for word in words:
        output+=emojis.get(word,word)+" "
    return output


msg=input("--> ")
print(emoji_converter(msg))

#
def greet_user(nam,last_name):
    print(f"Hi there {nam} {last_name}!")#When we run the function these 2 lines run
    print('Welcome Abroad')
#
#
print("Start")
greet_user(last_name="smith",nam="John")
#Keyword argument to improve readability
print("Finish")                              #Use postional argument at first then u can use keyword arguments

#
def square(number):
    return number*number


print(square(3))
#
def emoji_converter(msg):
    words=msg.split(' ')
    emojis={
        ":)":"😊",
        ";9":"😘",
        ":(":"😒"
    }
    output=""
    for word in words:
        output+=emojis.get(word,word)+" "
    return output


msg=input("--> ")
print(emoji_converter(msg))

#Exceptions
try:
    age=int(input("Enter age= "))
    income=20000
    risk=income/age
    print(age)
except ZeroDivisionError:
    print('age cannnot be zero')
except ValueError:
    print("invalid input")

#
class Point:

    def move(self):
        print("move")

    def draw(self):
        print("draw")
point1=Point()
point1.x=10
point1.y=20
print(point1.x)
point1.draw()

point2=Point()
point2.x=1
print(point2.x)
#
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

point = Point(10, 20)
print(point.x)
#
class Person:
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f"Hi, I am {self.name}")


john=Person("John Smith")
john.talk()

bob=Person("Bob Smith")
bob.talk()
#
class Dog:          ########
    def walk(self):        #
        print("Walk")      #
                           # ------> Very repetetive process so we need to  make it less
                           #                      (The solution)
class Cat:                 #                            |
    def walk(self): ########                            |
        print('walk')#                                  |
#                                                       |
class Mammal:                                  #<_______|
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass    #we can add other methods along with it too
class Cat(Mammal):
    def be_annoying(self):
        print("annoying")
    pass    #Same as above

dog1=Dog() #To print the output for dogs 
dog1.walk()

#Modules importing from other file
import converters
from converters import kg_to_lbs

# Using the imported function directly
print(kg_to_lbs(100))

# Using the module's namespace
print(converters.kg_to_lbs(70))
#

numbers=[10,6,4,2]
print(max)




