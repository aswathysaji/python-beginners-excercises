
l=[] #initialize an empty list
n=int(input("Enter the limit:"))
for i in range(0,n):
    x=int(input("no:"))
    l.append(x) #add values to the empty list
print(l)

#extend two list

l1=[1,2,3,4]
l2=[5,6,7,8]
(l1.extend(l2))
print(l1)

#concatenate two lists

l3=[0,9,8]
print(l1+l3)

# insert values

l3.insert(2,6)
print(l3)

#remove elements

l3.remove(6)
print(l3)

#poping an element

l3.pop(2)
print(l3)

#clear

l3.clear()
print(l3)

#del

del l1[2]
print(l1)