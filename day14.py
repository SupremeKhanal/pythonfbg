#return type function
def hello():
    return("Hello World")


hello()
#
def cal():
    V=0
    l=int(input("Enter L="))
    b=int(input("Enter b= "))
    a=l*b
    return a

area=cal()
print(area)
h=int(input("Enter H="))
V=area*h
print("Volume =",V)

#

def cal(l, b):
    area = l * b
    return area

l = int(input("Enter L = "))
b = int(input("Enter b = "))
h = int(input("Enter the Height = "))

area = cal(l, b)
v = area * h
print("Volume =", v)

#

