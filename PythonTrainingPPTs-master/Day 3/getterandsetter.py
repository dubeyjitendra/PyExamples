## Simple Objects

# class Car:
#
# 	def __init__(self, a=40):
# 		self.speed =a
#
# 	def get_speed(self):
# 		return self.speed
#
# 	def set_speed(self, a):
# 		self.speed =a
# 		return
#
# car = Car()
#print(car.speed)
#print(car.get_speed())
# print(car.set_speed(80))
# print(car.get_speed())

# print(car.speed)
# print(car.get_speed())
# car.set_speed(80)
# print(car.get_speed())
		
		
## 2 Encapsulation

# class Car:
#
# 	def __init__(self, a=40):
# 		self.__speed =a
#
# 	def get_speed(self):
# 		return self.__speed
#
# 	def set_speed(self, a):
# 		self.__speed =a
# 		return
#
# car = Car()
#
# #print(car.get_speed())
# car.set_speed(80)
# print(car.get_speed())
# print(car.__speed)



## 3 
class Car:

	def __init__(self, a=40):
		self.__speed =a

	def get_speed(self):
		return self.__speed

	def set_speed(self, a):
		if a <= 0 or a>= 160:
			print("speed needs to 0 to 160")

		else:
			self.__speed =a

car = Car()
car.set_speed(-80)

