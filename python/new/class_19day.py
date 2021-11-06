## Polymorphism

"""
1- complie time Polymorphism (method overloading)
2- run time  Polymorphism (Method overriding)
"""


#1- method overloading

# class Animal:
#
#     def run(self,name):
#         print(f'name is  {name}')
#
#     def run(self,name,age):
#         print(f'name is  {name}  and age is {age}')
#
# obj = Animal()
# obj.run("John",45)

### method overriding

class A:
    def dance(self,name):
        print(f'i can dance {name}')

class B(A):
    def dance(self,name):
        print(f'modified function name, i can dance {name}')

# obj = B()
# obj.dance("John")