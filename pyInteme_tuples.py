# Tuple: ordered, inmutable, allows duplicate elements
mytuple="Max", 28, "Boston" #The parenthesis are optional
print(mytuple)

isNotTuple=("Max")
print(type(isNotTuple))

isTuple=("Max",)
print(type(isTuple))

my_tuple=tuple(["Max",28,"Boston"])
print(my_tuple)

item=my_tuple[-2] #the second last item
print(item)

my_tuple[0]=="Tim"
print(my_tuple[0]) # It's not posible change an tuple's item
# 'tuple' object does not support item assignment. Tuple is inmutable

for elem in my_tuple:
    print(elem)

if "Max" in my_tuple: #To verify if an element is in tuple
    print("yes")
else:
    print("no")

myTuple=('a','p','p','l','e')
print(len(myTuple))
print(myTuple.count('p')) #Count an element
print(myTuple.index('a')) #To know the item index

myList=list(myTuple) # To convert tuple to list
print(myList)

myTuple2=tuple(myList) # To convert list to tuple
print(myTuple2)

b=myTuple2[2:5]
print(b)

c=myTuple[::2] #Elements 2 in 2
print(c)

reverseTuple=myTuple[::-1]
print(reverseTuple)

peopleTuple=("Max", 28,"Boston") #Unpacking tuple
name, age, city=peopleTuple #variables quantity should be equal to tuple's items quantiy

print(name)
print(age)
print(city)

numTuple=(0,1,2,3,4)
i1, *i2, i3=numTuple
print(i1)
print(i2) #different if print with '*'
print(i3)


#size of tuple is minor than size of list for the same elements
import sys
my_list=[0,1,2,"Hello",True]
my_tuple=(0,1,2,"Hello",True)
print(sys.getsizeof(my_list),"bytes")
print(sys.getsizeof(my_tuple),"bytes")


#It's more efficient iterate over a tuple than over a list
import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))













