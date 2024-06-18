info=""
n=int(input("Ener N= "))
for i in range(1,n+1):
    name=input("Enter name= ")
    age=int(input("Enter age = "))
    add=input("Enter Adress= ")
    phone=input("Enter phone= ")
    info=info+f"{name},{age},{add},{phone}\n"

file=open("info.csv",'w')
file.write("sn,name,age,add,phone\n")
file.write(info)
file.close()

import panda as pd
df=pd.read_csv("info.csv")
print(df)