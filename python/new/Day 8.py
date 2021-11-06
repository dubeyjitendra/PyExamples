### 8.Loop and Control Statement

# Control Statement
# if
# elif
# else

## loop
# while
# for

## Loop Control Statements
# break
# continue
# pass


# a,b = 100,200
#
# if a > b:
#     print("a is greater than b")
# elif b > a:
#     print("b is greater than a")
# else:
#     print("a and b are same")
#
# ## ternary operator
# print("a is greater than b" if a > b else "b is greater than a" if b > a else "a and b are same")

## Questions
## age & salary(ram & shyam)

## loop
# i=0
# while True:
#     i = i+1
#     print(i)

# i = 0
# while i < 10:
#     i = i+1
#     print(i)

# use a While loop to print below pyramids
# i=1
# while i < 10:
#     j=1
#     while j <= i:
#         print("*", end=" ")
#         j += 1
#     print()
#     i += 1
# *
# * *
# *  *  *
# *  *  *  *
# *   *  *  *  *
####

### for loop

# synatx:
# for <variable> <membership> <sequence datetype>:
#     statement

###########
print("Using for loop======================")
# for i in range(1,10):
#     for j in range(1,i):
#         print("*" ,end=" ")
#     print("")


## salry
lst  = ["1000","2000","30000","1000","2000","30000"]

### Max
# for i in range(len(lst)-1):
#     if lst[i] == lst[i+1]:
#         print("lst",lst[i])
#     elif lst[i] < lst[i+1]:
#         print("lst", lst[i+1])
#     elif lst[i] > lst[i+1]:
#         print("lst", lst[i])
#
# print(max(lst))


## pass  ignore the statement
## break

lst  = ["1000","2000","30000","1000","2000","30000"]

# for i in lst:
#     if i=="30000":
#         break ## terminate
#     print("=== running ")
#
# print("just checking")

# for i in lst:
#     if i=="30000":
#         print("Grade A")
#         continue




# age=4
# if age < 10:
#     pass

# def fib(n): ## recursive function
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
#
# print(fib(10))
#10 ==index

# for i in "siddesh":
#     if i == "e":
#         print("continue operation is going on")
#         continue
#     print(i)

# for i in "sidd":
#     if i =="i":
#         pass
#     else:
#         print(i)


# 1- max
# 2- min
# 3- fib
# 4- left side print *
# 5- center side print *


######
# def max_func(lst):
#     max_values = 0
#     for i in range(len(lst)-1):
#         if i==0:
#             max_values = lst[i]
#             continue
#         if lst[i] > max_values:
#             max_values=lst[i]
#     return max_values
#
# def min_func(lst):
#     min_values = 0
#     for i in range(len(lst)-1):
#         if i==0:
#             min_values = lst[i]
#             continue
#         if lst[i] < min_values:
#             min_values=lst[i]
#     return min_values

# lst=[10,5,3,7,9,10,10,3,4,5,56,78,89,988,990,9090,334,3434,43,4,3,3,43,43]
# print(max_func(lst))
# print(min_func(lst))

# use a While loop to print below pyramids
# i=1
# while i < 10:
#     j=1
#     while i <= j:
#         print(" ")
#         print("  *",end=" ")
#         j += 1
#     print()
#     i += 1

## right
# for i in range(1,10):
#     for j in range(1,i):
#         print("*",end=" ")
#     print()

## center
def cent(rows):
    k = 0
    for i in range(1, rows + 1):
        for space in range(1, (rows - i) + 1):
            print(end="  ")
        while k != 2 * i:
            print("* ", end="")
            k += 1

        k = 0
        print("\r") #

cent(10)
#1,10  1,2,3,4,5,6,7,8,9,10
#1,3 # 1,2


# k = 0
# for i in range(1, 10 + 1):
#     ## 9  space create
#     for space in range(1, (10 - 1) + 1):
#         print(end="  ")
#     while k != (2 * i - 1):
#         print("* ", end="")
#         k += 1
#
#     k = 0
#     print()

#
# ## leeft
#
# # Function to demonstrate printing pattern
# def left_value(n):
#     k = 2 * n - 2
#     for i in range(0, n):
#         for j in range(0, k):
#             print(end=" ")
#         k = k - 2
#         for j in range(0, i + 1):
#             # printing stars
#             print("* ", end="")
#         print("\r")
# #
# #
# # # Driver Code
# n = 5
# left_value(n)

























