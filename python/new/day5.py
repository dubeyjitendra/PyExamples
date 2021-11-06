###
my = "Hello"
my1 = "world"

name = my +" "+ my1 # addition of two variable of strings
#print(name)


## multiple

name2 = (my * 3)
# print(name2)

###
x= "my name is sid"
# x= x + " I live in Mumbai"
# print(x)
# x= x.replace("sid","nitesh")
# print(x)




## Range

# print(len(x))
# x= x[2:4]
# print(x)

# print(x[:-3])
#print(x[:])
x= "my name is sid"
x= "my na"
#x= " name is"
# print(x[3:5])
#●	Escape Characters

x = "Hello \nworld"
# print(x)
x = "Hello \tworld"
# print(x)
x = "Hello \rworld"
# print(x)
##"hello  world"


### ●	String Formatting Operator
# county ="India is a great country"
# print("name:"+county)
# print(f"name : {county}")
# print("name : {}".format(county))
# print("name :%s"%county)

## unicode
name3 = u"sid"
# print(name3)
# print(type(name3))

##
#capital letter
name4= "rishab"
# print(name4.capitalize())
# print(name4.upper())
name5= "RISHAB"
# print(name5.swapcase())
print(name5.lower())

lst =["my","name","is","india"]
# s= " ".join(lst)
# print(s)
#
# print(max(lst))
# print(min(lst))

x= "my name is india, @india is a great country"
# print(x.count("india")) ## totsl number of times occor a perticular
# print(x.find("great")) ##index

x= x.split(" ")
print(x)


#############
#[on_true] if [expression] else [on_false]

a,b=10,20

m= a if a< b else b
print(a)
## using
print( (b, a) [a < b] )

# Python program to demonstrate nested ternary operator
a, b = 10, 20

print("Both a and b are equal" if a == b else "a is greater than b"if a > b else "b is greater than a")