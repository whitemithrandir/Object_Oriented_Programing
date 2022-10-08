class Employee:
    pass
employer1 = Employee()

# attribute
class Footballer:
    age = 30
    club = "besiktas"

f1 = Footballer()
print(f1)
# print(f1.age)
# print(f1.club)
f1.club = "fenerbahce"
print(f1.club)


######################################################################
#methods
class Square(object):
    edge = 5
    area = 0
    def area(self):
        self.area = self.edge*self.edge
        print(self.area)

s1 = Square()
print(s1)
print(s1.edge)

s1.edge = 7
s1.area()

class emp(object):
    age = 25
    salary=10500

    def AgeSalaryRatio(self): #method
        a= self.salary / self.age
        print("method:", a )

def AgeSalaryRatio(salary , age): #fonksiyon
    b =salary / age
    print("function:", b)

E1 = emp()
E1.AgeSalaryRatio()
AgeSalaryRatio(13500,25)

def findArea(a,b):
    area = a*b**2
    return area
result1 = findArea(3.14,5)
result2 = findArea(3.14,10)
print(result1+result2)


######################################################################
### constructer or initializer

class Animal(object):

    #method
    def __init__(self,a,b): #(name,age) = (a,b) = ("dog", 25)
        self.name = a
        self.age = b

    # method
    def getName(self):
        print(self.name)

    # method
    def getAge(self):
        print(self.age)

a1 = Animal("dog", 25)
a2 = Animal("cat", 20)
print(a1)
print(a2)
a1.getName()
a2.getAge()

##calculator project

class Calc(object):
    "calculator"

    #init method
    def __init__(self,a,b):
        "initialize values"
        #attribute

        self.value1 = a
        self.value2 = b

    #method
    def add(self):
        "addition a+b "
        return self.value1 + self.value2

    # method
    def mult(self):
        "multiply a*b"
        return self.value1 * self.value2

    def div(self):
        "division a/b"
        return self.value1 / self.value2

v1 = int(input("1.deger gir: "))
v2 = int(input("2.deger gir: "))
c1 = Calc(v1,v2)
x = c1.add()
y = c1.mult()
z = c1.div()

print("Add: {}, Multiply: {}, Division: {}".format(x,y,z))

######################################################################

###Emcapsulation/kapsülleme
#belirli class içerisindeki attribute'lara methodlara dışarıdan engellenmesi buradaki amaç

class BankAccount(object):

    def __init__(self,name,money,address):
        self.name = name #global
        self.__money = money #private
        self.address = address

    #get and set global
    def getMoney(self):
        return self.__money

    def setMoney(self,amount):
        self.__money = amount

    #private
    def __increase(self):
        self.__money = self.__money + 500

p1= BankAccount("saban", 380000, "umraniye")
p2= BankAccount("ahmet", 1000, "beykoz")

print(p1.name)
print("get method:", p1.getMoney())

p1.setMoney(20000)
print("after set method:", p1.getMoney())

p1.__increase()
print("after increase:", p1.getMoney())

######################################################################

#  Miras/inheritance

#parents
class Animal(object):
    def __init__(self):
        print("animal is created")

    def toString(self):
        print("animal")

    def walk(self):
        print("animal is walking")
#child
class Monkey(Animal):
    def __init__(self):
        super().__init__() #use init of parent(animal) class
        print("monkey is created")

    # def toString(self):
    #     print("monkey")

    def climb(self):
        print("monkey can climb")

m1 = Monkey()
# m1.climb()
# m1.walk()

m1.toString()


#####################################################################

# inheritance Project

class Website(object):
    "parent"
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

    def loginInfo(self):
        print(self.name + " " + self.surname)

class Website2(Website):
    "child"
    def __init__(self, name, surname,ids):
        Website.__init__(self, name, surname)
        # super().__init__()  # use init of parent(child) class
        self.ids = ids

    def login(self):
        print(self.name + " " + self.surname + " " + self.ids)

class Website3(Website):

    def __init__(self, name, surname, mail):
        Website.__init__(self, name, surname)
        self.mail = mail

    def login(self):
        print(self.name + " " + self.surname + " " + self.mail)

p1 = Website("saban", "kara")
p2 = Website2("david", "beckham","132")
p3 = Website3("mahmut","tuncer", "@hotmail")

p1.loginInfo()
p2.login()
p2.loginInfo()
p3.login()
p3.loginInfo()



######################################################################

# Soyut sınıflar/Abstrack classes
"nesne yönelimli programlama da nesnesi yaratılamayan sınıflara verilen isim"

from abc import ABC, abstractmethod, ABCMeta
#abstract class
class Animal(metaclass=ABCMeta): #super class

    @abstractmethod
    def walk(self): pass

    @abstractmethod
    def run(self):
        print("sadf")

    "abstract class iki şartı var"
    "abstract class hiçbir şekilde instance yaratamayacak "
    "abstract class içinde kullanılan metodlar sub classlarda da kullanılmak zorunda"
    "amaç nerede hangi fonsksiyonu nerede kullanacağını baştan belirlemek "

#sub class
class Bird(Animal):

    def __init__(self):
        print("bird")

    def walk(self):
        print("walk")

    def run(self):
        print("run")

b1 = Bird()
b1.run()



#####################################################################

# Overriding

#super class
class Animal:

    def toString(self):
        print("animal")
#sub class
class Monkey(Animal):

    def toString(self):
        print("monkey")

a1 = Animal()
a1.toString()

m1 = Monkey()
m1.toString() #monkey calls overriding method

######################################################################
# Overriding prohect

class Rectangle():
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
        print("çalıştı 1")

    def getArea(self):
        print(self.length*self.breadth," is area of rectangle")

class Square(Rectangle):
    def __init__(self,side):
        self.side = side
        print("çalıştı 3")
        Rectangle.__init__(self,side,side)
        print("çalıştı 2")

    def getArea(self):
        print(self.side*self.side," is area of square")

s = Square(4)
s.getArea()

print("\n")
r = Rectangle(2,4)
r.getArea()

######################################################################
#Çok Şekillilik/Polymorphism
"aslında burada overriding yapılıyor, superclassdaki metod sub classlarda da kullanılıyor"
class Employee():

    def raisee(self):
        raise_rate = 0.1
        result = 100 + 100*raise_rate
        print("super class: ", result)

class ComEng(Employee):

    def raisee(self):
        raise_rate = 0.2
        result = 100 + 100*raise_rate
        print("sub class for ComEng: ", result)


class ElmEng(Employee):

    def raisee(self):
        raise_rate = 0.3
        result = 100 + 100 * raise_rate
        print("sub class for ElmEng: ", result)

e1 = Employee()
c1 = ComEng()
ee1 = ElmEng()

# e1.raisee()
# c1.raisee()
# ee1.raisee()

employee_list = [e1, c1, ee1]

for i in employee_list:
    i.raisee()

######################################################################

# final project

from abc import ABC, abstractmethod
class Shape(ABC):
    """
    Shape = super class / abstract class
    """
    #abstract method
    @abstractmethod #buradaki def'ler aşağıdaki diğer classlarda kullanılmak zorunda
    def area(self): pass

    @abstractmethod
    def perimeter(self): pass

    #overriding and polymorphism
    def toString(self): pass

#child
class Square(Shape):
    "Sub class"

    def __init__(self,edge):
        self.__edge = edge #encapsulation private attibute

    def area(self):
        result = self.__edge**2
        print("square ares: ", result)

    def perimeter(self):
        result = self.__edge * 4
        print("square perimeter: ", result)

    # overriding and polymorphism
    def toString(self):
        print("square edge: ", self.__edge)

class Circle(Shape):
    "ciscle class"

    # constant variable
    PI = 3.14

    def __init__(self,radius):
        self.__radius = radius

    def area(self):
        result = self.PI*self.__radius**2  #pi*r^2
        print("circle area: ", result)

    def perimeter(self):
        result = 2*self.PI*self.__radius #2*pi*r
        print("circle perimeter: ", result)

    # overriding and polymorphism
    def toString(self):
        print("circle radius: ", self.__radius)

s = Square(5)
# s.area()
# s.perimeter()
# s.toString()

c = Circle(3)
# c.area()
# c.perimeter()
# c.toString()

list = [s,c]

for i in list:
    i.area()
    i.perimeter()
    i.toString()

#####################################################################
rent a vahicle project

import datetime
#parent class
class VahicleRent:

    def __init__(self,stock):
        self.stock = stock
        self.now = 0

    def displayStock(self):
        """
            display stock
        """
        print("{} vehicle available to rent".format(self.stock))
        return self.stock

    def rentHourly(self,n):
        """
            rent hourly
        """
        if n <=0:
            print("number shold be positive")
            return None

        elif n>self.stock:
            print("sorry, {} vehivle available to rent ".format(self.stock))

        else:
            self.now = datetime.datetime.now()
            print("rented a {} vahicle for hourly at {} hours".format(n,self.now.hour))

            self.stock = self.stock - n

            return self.now

    def rentDaily(self,n):
        """
            rent daily
        """
        if n <= 0:
            print("number shold be positive")
            return None

        elif n > self.stock:
            print("sorry, {} vehivle available to rent ".format(self.stock))

        else:
            self.now = datetime.datetime.now()
            print("rented a {} vahicle for daily at {} hours".format(n, self.now.hour))

            self.stock = self.stock - n

            return self.now

    def returnVehicle(self, request,brand):
        """
        return a bill
        brand = kiralanan araç
        """
        car_h_price = 10
        car_d_price = car_h_price*8/10*24
        bike_h_price = 5
        bike_d_price = bike_h_price*7/10*24

        rentalTime, rentalBasis, numOfVehicle = request
        bill = 0 #fatura

        if brand == "car":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock = self.stock + numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime

                if rentalBasis == 1: #hourly
                    bill = rentalPeriod.seconds/3600*car_h_price*numOfVehicle

                elif rentalBasis == 2: #daily
                    bill = rentalPeriod.seconds/(3600*24)*car_d_price*numOfVehicle

                if(2 <= numOfVehicle):
                    print("you hve extra 20% discount")
                    bill = bill*0.8

                print("thank you for returning your car")
                print("price: ${}".format(bill))
                return bill

        elif brand == "bike":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock = self.stock + numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime

                if rentalBasis == 1: #hourly
                    bill = rentalPeriod.seconds/3600*bike_h_price*numOfVehicle

                elif rentalBasis == 2: #daily
                    bill = rentalPeriod.seconds/(3600*24)*bike_d_price*numOfVehicle

                if(2 <= numOfVehicle):
                    print("you hve extra 30% discount")
                    bill = bill*0.7

                print("thank you for returning your bike")
                print("price: ${}".format(bill))
                return bill

        else:
            print("you do not rent a vehicle")
            return None

#child class 1
class CarRent(VahicleRent):

    global discount_rate
    discount_rate = 15
    def __init__(self,stock):
        super().__init__(stock)

    def discount(self,b):
        """
            discount
        """
        bill = b - (b*discount_rate)/100
        return bill

#child class 2
class BikeRent(VahicleRent):

    def __init__(self,stock):
        super().__init__(stock)

#customer
class Customer:
    def __init__(self):
        #reantalBasis saatlik mi günlük mü kiraladı
        self.bikes = 0
        self.rentalBasis_b = 0
        self.rentalTime_b = 0

        self.cars = 0
        self.rentalBasis_c = 0
        self.rentalTime_c = 0

    def requestVehicle(self,brand):
        """
            take a request bike or car from customer
        """
        if brand == "bike":
            bikes = input("how many bikes would you like to rent?")

            try:
                bikes = int(bikes)
            except ValueError:
                print("number should be number")
                return -1

            if bikes <1:
                print("number of bikes should be greater than zero")
                return -1

            else:
                self.bikes = bikes
            return self.bikes

        elif brand == "car":

            cars = input("how many cars would you like to rent?")
            try:
                cars = int(cars)
            except ValueError:
                print("number should be number")
                return -1

            if cars <1:
                print("number of cars should be greater than zero")
                return -1
            else:
                self.cars = cars
            return self.cars

        else:
            print("request vehicle error")


    def returnVehicle(self, brand):
        """
            return bikes or cars
        """
        if brand =="bike":
            if self.rentalTime_b and self.rentalBasis_b and self.bikes:
                return self.rentalTime_b , self.rentalBasis_b , self.bikes
            else:
                return 0,0,0
        #eğer bunlardan herhangi biri yoksa 0 döndür
        elif brand == "cars":
            if self.rentalTime_c and self.rentalBasis_c and self.cars:
                return self.rentalTime_c , self.rentalBasis_c , self.cars
            else:
                return 0,0,0

        else:
            print("request vehicle error")



