# Clases and Objects
import numpy
np = numpy

person1 = {}
person1 ["Name"]= 'Dalen Bean'
person1['Age'] = 23
person1['Major'] = 'MIS'

person1['HW_Grades'] = [49.5, 48, 50]

print(person1)
# person1['Calc_HW_Grade'] = def Calc_HW_Grade(grades); return np.mean()
# you can't put a function into a dictionary, you need to put it into a class

class Person():
    def __init__(self, name, age, major, HW_Grades):
        self.name = name
        self.age = age
        self.major = major
        self.HW_Grades = HW_Grades
    
    def calc_hw_grade(self):
        return np.mean(self.HW_Grades)

person1 = Person('Ethan', 22, 'MIS', [45, 49, 48.5])

print(person1)

print(person1.name)
print(person1.age)
print(person1.major)
print(person1.HW_Grades)
print(person1.calc_hw_grade())

person2 = Person('Liz', 19, 'MDATA', [50, 50, 50])

print(person2)

print(person2.name)
print(person2.age)
print(person2.major)
print(person2.HW_Grades)
print(person2.calc_hw_grade())



class Student:
    def __init__(self, anum, name):
        self.__anum = anum
        self.name = name
        
    def get_anum(self):
        return self.__anum
    
    def set_anum(self, anum):
        self.__anum = anum
        
    def get_name(self):
        return self.name
        
    def set_name(self, name):
        self.name = name
        
student1 = Student('1234', 'Liam')
print(student1.name)
# print(student1.__anum)

# Inheritance and ploynomance

class Car:
        def __init__(self, make, model, year, price):
            self.make = make
            self.model = model
            self.year = year
            self.price = price
        
        def calc_value(self, current_year):
            return self.price * 0.9 **(current_year - self.year)

class AntiqueCar(Car):
    # def __init__(self):
    #     pass
    
    def calc_value(self, current_year):
        return self.price * 1.05 ** (current_year - self.year)
    
andy_car = Car('Toyota', 'Sequoia', 2021, 15000)
mw_car = Car('Ford', 'F-150', 2016, 28000)

liz_car = AntiqueCar('Chevrolet', 'Blazer', 1972, 5000)

my_cars = [andy_car, mw_car, liz_car]

total_value = 0
for car in my_cars:
        total_value += car.calc_value(2021)
    
print('Value of the entire car lot is:', total_value)