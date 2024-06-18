l=["fish","banana","apple","fish","fish"]

seen=[]
for item in l:
    if item not in seen:
        seen.append(item)
print("Original list",l)
print("The updated list is",seen)
#
l=["fish","fish","banana","fish","apple","fish","fish"]
s=l
D=" "
print(s)
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if s[i]==l[j]:
            D=D+ " "+str(j)
            break
print("Indices with duplicate data are",D)
#



