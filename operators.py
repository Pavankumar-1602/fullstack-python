product_price = 5000
delivery_charges =100

total = product_price +delivery_charges
print(total)



######
a = 10
b = 3

print (a+b)
print (a-b)
print (a*b)
print (a/b)
print (a // b)
print (a%b)
print (a**b)

student = 10
groups = 2

print(student // groups)

#################(assind operations)
followers = 100
followers = followers + 1
print(followers)
#############(comparison operation)==,!=,>,<,>=,<=

saved_pasword ="123abcd"
enterd_pasword = "123abcd"
print(saved_pasword == enterd_pasword)

##############(logical operations)

balance = 1100
pin_correct =True
if balance >= 1000 and pin_correct:
    print("Withdraw allowed")
else:
    print("failde")
    
    
################
  
item =input("enter the item name:")
price = float(input("enter the item price:"))
qutantity = int(input("enter the item quantity:"))

total = price * qutantity

print(item)
print(price)
print(qutantity)
print(total)

##############
age = 25
salary = 50000
if age > 18 and salary > 30000:
    print("loan approved")
    
    #############################
    day ="sunday"
    if day == "sunday" or day == "saturday":
        print("weekend")
    ###########################
    
    
    
    
    
    
    
 ######################
    def withdraw_money():
        pin = int(input("Enter your pin:"))
        if pin == 1234:
            amount=int(input("Enter the amount to withdraw:"))
            balance = 10000
            if amount <= balance:
                balance = balance - amount
                print("withdraw successful")
                print("remaining balance:", balance)
            else:
                print("insufficient balance")
            
        else:
            print("incorrect pin")
            
    withdraw_money()       
    
####################################################(list)
    users=["dinga","dinge","peng"]
    for users in users:
        print("message sent to", users)
        
        
############################
    name = "doni"
    
    
    for ch in name:
        print(ch)
        
##########################
for i in range(10):
    if i == 5:
        continue
    print(i)
    
###########################
pasword = " "
while password != "1234":
    password =input("Enter your password:")
    print("login success")
    
    student1 ="ram"
    student1 ="sam"
    student1 ="dina"
############################
student =[ 
          "ram",
          "sam",
          "dina"
]
student.append("alex")
student.remove("sam")
print(student)

#############################