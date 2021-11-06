# Dictionary Lectures

#Define :  { "K1": 1,"K2":2,"K1":3}
# Syntax
#  Keys :Values

#Important Notes:
# Key is separated it values by colon
# All items in dictionary separated by comma
#  whole dictionary is Enclosed by curly brackets
# Keys is immutable python objects, It means can not be changed while creating
# Values can be change, becuase it is mutuable python objects
# Keys are using String ,Numbers and Tuples for defining data types.
# Keys are unique in python objects. Please don't create same key on dictionary once again.
# Values can not hold more than one value.
# define same keys in dictionary it hold last keys

# defined dictionary
mydict={"Name":"John", "Age": 35, "Salary": 3000}
mydict1={"Name":"John", "Age": 35, "Salary": 3000}
# Accessing dictionary
#print(mydict) # Print all dictinary items
#print(mydict["Name"]) # Printing single item from dictionary
#print(mydict.items())  # Print all items in tuple format
#print(mydict[0]) # it showing errror while calling,dictionary not taken index value its hold name of column

# Updating Dictionary
#mydict1={"Country": "India"} #
#mydict2={"Country": "USA"} # Can change by run time after defining key and values
#mydict.update(mydict1)
#mydict.update(mydict2)
#print(mydict)

# Delete Dictionary Elements

# Delete all items from Dictionary using del with name of dictionary
# We can delete single keys from Dictionary using name of Dictionary with key

#del mydict
#print(mydict) # Return error becuase delete has been deleted on above statement

# Single key deleted from Dictionary
#del mydict["Age"]
#print(mydict)  # Deleted single records from Dictionary

# Clear Dictionary
#mydict.clear() #
#print(mydict)  # All item will be deleted  from Dictionary but struture can not be deleted.

#Built-in Dictionary Functions
# len
# str
# type
# cmr
#print(len(mydict)) # Find count of dictionary Items
#print(str(mydict))   # Covert dictionary to sting
#print(type(str(mydict))) # Find type of any values
# Built-in Dictionary Method
#print(mydict.clear()) # CLear all items in dictionary


# Copy Method
#dictcopy={}
mydict1 = mydict.copy()
#print(dictcopy)
#print(mydict1)


# Compare dictionary
#d1={"a":1 ,"b":2,"z":3}
#d2={"b":1 ,"c":2,"a":3}
#print({d1:d2["a"]})
'''d= {key:d1[key] for key in d1 if key in d2}
print(d)
print("a" in d2)

for key in d1:
    print(key)'''


# FROMKEYS
#print(mydict.fromkeys(mydict))

#for item  in mydict.fromkeys(mydict):
#   print(item)
# VAlues
#print(mydict.values())
#for i in mydict.values():
  #  print(i)

# Get method
#print(mydict.get("Age"))

# SetDefault
#mydict.setdefault("Dept","Science")
#print(mydict)
# Program
#*
# * *
'''k=0
row=10
for i in range(1,row+1): # It was iterating one bye one
    for j in range(0,(row)): # It was running 10 times and added to print values
        print("1",end="")
    while k !=(i):  # It is perform ervery time based on i (Increasement) values
        print("*", end="")
        k=k+1
    k=0
    row = row - 1
    print()'''
# End Program
