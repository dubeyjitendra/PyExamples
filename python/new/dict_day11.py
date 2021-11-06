# k = 0
# for i in range(1, 10 + 1):
#     for space in range(1, (10 - i) + 1):
#         print(end="  ")
#     while k != 2 * i:
#         print("* ", end="")
#         k += 1
#     k = 0
#     print("\r")


### dict
## syntax
#{key : value}

dict= {1:2,2:4,"age":26,"name":"sid"}

### accessing the value from dictionary
# print(dict)
# print(dict['age'])
# print(dict['name'])
# print(dict[1])

### add item
# dict["college"] = "ABC"
# print(dict)

### update
# dict["college"] = "NMS vashi, Navi Mumbai"
# print(dict)

# dict1= {"college":"NMS vashi, Navi Mumbai 2"}
# dict.update(dict1)
# print(dict)


# print(dict)
# print("age" in dict)

## delete
dict2= {1:2,2:4,"age":26,"name":"sid","name":"rushab","name":"nitesh"}
#print(dict["name"])

# del dict['name']
# print(dict)

# del dict2
# print(dict2)

# dict2.pop("age") ## delete
# print(dict2)

# dict2.clear()
# print(dict2)

### loop
# for (k,v) in dict2.items():
#     print((k,v))

# for k in dict2.keys():
#     print(k)

# for v in dict2.values():
#     print(v)


# print(len(dict2))

dict3 =dict2.copy()
dict3["salry"]=1000
print(dict3)



################ Questions

# 1- check if a value 200 exist in dictiinary.
sampledict = {'a': 100, 'b': 200, 'c': 300}

# 2 rename key city values
s = {"name": "John", "age": 45, "city": "Mumbai"}

# 3 Below are the two lists convert it into the dictionary
"""keys = ['Ten', 'Twenty', 'Thirty']
   values = [10, 20, 30]
   
"""

# 4 Merge following two Python dictionaries into one
"""
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
"""

# 5 Delete set of keys from a dictionary
"""
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keysToRemove = ["name", "salary"]
"""





