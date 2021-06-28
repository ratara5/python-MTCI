# Lists: ordered, mutable, allows duplicate elements
myList=["banana", "cherry", "apple"]
print(myList)

myList2=[5, True, "apple", "apple"]
print(myList2)

item=myList[0]
item=myList[-2]
print(item)

for i in myList2:
    print(i)

if True in myList2:
    print("yes")
else:
    print("no")

print(len(myList))
myList.append("lemon")
print(myList)

myList.insert(0, "cononut")
print(myList)

myList.pop()
print(myList)

myList.remove("banana")
print(myList)

# myList.clear() #return empty list

myList3=[ "Arnoldo", "Zebedeo"]

myList3.sort() # TypeError: '<' not supported between instances of 'str' and 'bool'
print(myList3)

myList4=[-9, 15, -8, 13, 2, 0]
new_list=sorted(myList4)
print(new_list==myList4) # function sorted generate a new list

myList5=[0]*5+[i**2+1 for i in range(0,11)]
print(myList5)

a=myList5[5:10]
print(a)

b=myList5[::-1]
print(b)

list_1 = ["apple", "banana", "cherry"]
list_copy = list_1
list_copy.append("pineapple")
print(list_1 != list_copy) #list assignements don't generate a new list
# better list.copy()
list_copy_now=list_1.copy()
list_copy_now.append("pineapple")
print(list_1 != list_copy_now) #now both list are different, only later to aggregate aa new item in the copy!
# alternative
list_copy=list(list_1)
list_copy=list_1[:]
list_copy.append("pineapple")
print(list_1 != list_copy) #now both list are different, only after to aggregate a new item in the copy!

#list comprehension
myList6=[i for i in range(0,21)]
print(myList6)
myList7=[x**(2+x) for x in myList6]
print(myList7)
