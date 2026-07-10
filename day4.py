
# ############################################(class - biur print of object  /  object -reprasentation of class) # class student: #class name 

#    name = "ram"       # attribute
#    def study(self):#(def is a function)
#        print(" ram is a student")
# s1 = student()# object
# print(s1.name)  
# s1.study()# study is a method


# class student: #class name
#     def details(self):
#         print("had breakfast")
# s1=student()
# s1.details()# details is a method

# # # student.details(s1)

# #############################################(constracter)class Person:(init is constructer)
# class student:
#     def __init__(self, name, age):#
#         self.name = name
#         self.age = age
# s1 = student("dinga",22)
# s2 = student("ram",33)
# s3 = student ("sam ",21)
# print(s1.name, s2.name ,s3.name)
# print(s1.age, s2.age,s3.age)
# # ##############################################
# class bank :
#     def _init_(self,balance):
#         self.balance = balance
        
#         def check_balance(self):  ##(balance ,check balance - methods)
#             print(self.balance)
            
# account = bank(5000)
# account.check_balance()

###############################################
# class user:
#     def __init__(self,name):
#         self.name=name
#     def login(self):
#         print(self.name,"login in ")
        
# u1=user("nibba")
# u2=user("nibbi")
# u1.login()
# u2.login()
###############################################(single inheritance)
# class father:
#     def house(self):
#         print("father has a house")
# class son(father):
#     def bike(self):
#         print("son has a bike")
        
# s=son()
# s.house()
# s.bike()
############################################(multiple level inheritance)
# class appa:
#     def house(self):
#         print("appa's house")
# class amma:
#     def car(self):
#         print ("mom has a car")
# class son(appa,amma):
#     def bike(self):
#         print ("son has a bike")
        
# s1=son()
# s1.house()
# s1.car()
# s1.bike()

###########################################(heireke)
# class animal:
#     def __init__(self, name):
#         self.name = name

# class lion(animal):
#     def walk(self):
#         print(self.name, "lion is walking")

# class tiger(animal):
#     def walk(self):
#         print(self.name, "tiger is walking")

# class jaguar(animal):
#     def walk(self):
#         print(self.name, "jaguar is walking")     


# obj1 = lion("Simba")
# obj2 = tiger("Sher Khan")
# obj3 = jaguar("Shadow")


# obj1.walk()
# obj2.walk()
# obj3.walk()                   
###############################################      
        