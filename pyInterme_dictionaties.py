#Dictionary: Key-Value-pairs, Unordered, Mutable
mydict={"name":"Max", "age": 28, "city": "New York"}
print(mydict)

mydict2=dict(name="Mary", age=27, city="Boston")
print(mydict2)

value=mydict["city"]
print(value)

mydict["email"]="max@mail.com" #To add a new key-value pair
print(mydict)

mydict["email"]="max@xyz.com" #To change a value for a key
print(mydict)

