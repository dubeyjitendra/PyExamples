## Encap
# class Animal:
#
#     size = 10 ## class variable
#     __location = "Mumbai" ## class variable
#     def __init__(self,name,age):
#         self.name_name = name ## instance variable
#         self.age_age = age  ## instance variable
#
#     def __func(self,name_of_the_car):
#         print(f"car name is {name_of_the_car}")
#
#     def run(self):
#         return self.__func("Maruti")
#


# obj_animal= Animal("lion",40)
# obj_animal.run()
# # obj_animal.__func()
# print(obj_animal.size)



# OOPS:
# 1- Inheritance
# 2- class
# 3- Object
# 4- Encapsulation
# 5- Polymorphism

# class Display:
#
#     def disp(self):
#         print("hello")
#



### Inheritance

#1 single inheritance
## multi level inheritance
### multiple inheritance
#### Hierarchical inheritance
#### hybrid inheritance



#single inheritance

# class A:  ### father
#     print("A class Printed")
#     name = "SId"
#     def run(self):
#         return "Yes i can run"
#
#     def __add(self,a,b):
#         return a+b
#
# class B(A): ### child
#     print("B class Printed")
#
# objB = B()
# print(objB.run())

### Multi level inheritance

# class X(): ## grand father
#     def func1(self):
#         print("func1 is called")
#
#     def run(self,name,age):
#         print(f"my name is {name} and my age is {age}")
#
# class Y(X): ## father
#     def func2(self):
#         print("func2 is called")
#
# class Z(Y): ## child
#     def func3(self):
#         print("func3 is called")
#
#
# obj = Z()
# obj.run("john",30) ## X class
# obj.func2() ## Y class

### Multiple inheritance
# class X(): ## grand father
#     def func1(self):
#         print("func1 is called")
#
#     def run(self,name,age):
#         print(f"my name is {name} and my age is {age}")
#
# class Y(): ## father
#     def func4(self):
#         print("func2 is called")
#
# class M(): ## father
#     def func2(self):
#         print("func2 is called")
#
# class Z(X,Y,M): ## child
#     def func3(self):
#         print("func3 is called")
#
# obj = Z()
# obj.run("Ram",40)


### hierarchical inheritance


# class X(): ## parent
#     pass
#
# class Y(X):
#     pass
#
# class Z(X):
#     pass

### Hybrid inheritance

# class A:
#     pass
#
# class B(A):
#     pass
#
# class C():
#     pass
#
# class D(B,C):
#     pass
#
#
# obj = D()














# class My_error(Exception): ## single inhetance
#     print("this is my user defined error")

