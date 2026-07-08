# # # # # # # product_price = 5000
# # # # # # # delivery_charges =100

# # # # # # # total = product_price +delivery_charges
# # # # # # # print(total)



# # # # # # # ######
# # # # # # # a = 10
# # # # # # # b = 3

# # # # # # # print (a+b)
# # # # # # # print (a-b)
# # # # # # # print (a*b)
# # # # # # # print (a/b)
# # # # # # # print (a // b)
# # # # # # # print (a%b)
# # # # # # # print (a**b)

# # # # # # # student = 10
# # # # # # # groups = 2

# # # # # # # print(student // groups)

# # # # # # # #################(assind operations)
# # # # # # # followers = 100
# # # # # # # followers = followers + 1
# # # # # # # print(followers)
# # # # # # # # #############(comparison operation)==,!=,>,<,>=,<=

# # # # # # # # saved_pasword ="123abcd"
# # # # # # # # enterd_pasword = "123abcd"
# # # # # # # # print(saved_pasword == enterd_pasword)

# # # # # # # # ##############(logical operations)

# # # # # # # # balance = 1100
# # # # # # # # pin_correct =True
# # # # # # # # if balance >= 1000 and pin_correct:
# # # # # # # #     print("Withdraw allowed")
# # # # # # # # else:
# # # # # # # #     print("failde")
    
    
# # # # # # # # ################
  
# # # # # # # # item =input("enter the item name:")
# # # # # # # # price = float(input("enter the item price:"))
# # # # # # # # qutantity = int(input("enter the item quantity:"))

# # # # # # # # total = price * qutantity

# # # # # # # # print(item)
# # # # # # # # print(price)
# # # # # # # # print(qutantity)
# # # # # # # # print(total)

# # # # # # # # #########???
 
# # # # # # # #  #############################
# # # # # # # # day ="sunday"
# # # # # # # #     if day == "sunday" or day == "saturday":
# # # # # # # #         print("weekend")
# # # # # # # #  ###########################
    
    
    
    
    
    
    
# # # # # # # #  ######################
# # # # # # # #     def withdraw_money():
# # # # # # # #         pin = int(input("Enter your pin:"))
# # # # # # # #         if pin == 1234:
# # # # # # # #             amount=int(input("Enter the amount to withdraw:"))
# # # # # # # #             balance = 10000
# # # # # # # #             if amount <= balance:
# # # # # # # #                 balance = balance - amount
# # # # # # # #                 print("withdraw successful")
# # # # # # # #                 print("remaining balance:", balance)
# # # # # # # #             else:
# # # # # # # #                 print("insufficient balance")
            
# # # # # # # #         else:
# # # # # # # #             print("incorrect pin")
            
# # # # # # # #     withdraw_money()       
    
# # # # # # # # ####################################################(list)
# # # # # # # #     users=["dinga","dinge","peng"]
# # # # # # # #     for users in users:
# # # # # # # #         print("message sent to", users)
        
        
# # # # # # # # ############################
# # # # # # # #     name = "doni"
    
    
# # # # # # # #     for ch in name:
# # # # # # # #         print(ch)
        
# # # # # # # # ########################## 
# # # # # # # # for i in range(10):
# # # # # # # #     if i == 5:
# # # # # # # #         continue
# # # # # # # #     print(i)
    
# # # # # # # # ###########################
# # # # # # # # pasword = " "
# # # # # # # # while password != "1234":
# # # # # # # #     password =input("Enter your password:")
# # # # # # # #     print("login success")
    
# # # # # # # #     student1 ="ram"
# # # # # # # #     student1 ="sam"
# # # # # # # #     student1 ="dina"
# # # # # # # # ############################
# # # # # # # # student =[ 
# # # # # # # #           "ram",
# # # # # # # #           "sam",
# # # # # # # #           "dina"
# # # # # # # # ]
# # # # # # # # student.append("alex")
# # # # # # # # student.remove("sam")
# # # # # # # # print(student)

# # # # # # # #############################(tuppels are immutable we use that in () it start ccount from (3 2 1<-)
# # # # # # # student = ("ram","sam","dina")
# # # # # # # print(student[2])

# # # # # # # numbers = (1,2,3,4,5)
# # # # # # # print(numbers[0])

# # # # # # # data =(1,2,3)
# # # # # # # data [10] = 10
# # # # # # # print(data)
# # # # # # #############3(count operation in tupples)
# # # # # # x = (1,2,3,4,5,1,1,1,2,2,2,2,2)
# # # # # # print(x.count(2))
# # # # # # print(x.count(1))
# # # # # # print(x.count(3))

# # # #  X=("APPLE","MANGO","BANANA", "MANGO", "MANGO")
# # # #  print(X.count("MANGO"))
# # # #####################################(tupple sliceing)
# # # num = (10,20,30,40,50)
# # # print(num[0:4])
# # # #####################################(sets collection of uniqu valus , removile of duplicates this are representer by {} )

# # # x={1,2,3,2,1,1,1,5}
# # # print(x)
# # data ={1,2,3,8,9}
# # data.remove(9)
# # print(data)

# # a ={1,2,3}
# # # b ={3,4,5}
# # # print(a|b)

# # a={1,2,3}
# # b={3,4,5}
# # print(a&b)

# # ############################
# # def greeting():
# #     print("hello students")
# #     greeting()
# # #################################    
# # def DIV():
# #     return 10/20
# # # result = DIV()
# # # print(result)

# # ####################################(FUNCTION WITH ARGUMENTS )
# # def add(a,b): 
# #     print(a+b)
# # add(10,20)
# # ########################3333
# # def student(**details):
# #     print(details)
    
    
# # ##############################
# # def square(x):
# #      return x*x
# # print(square(16))
    
# # ###########################################    
# # add = lambda a,b : a+b
# # print(add(10,50))
# # # ####################################
# # add = lambda a,b : a+b
# # print(add(10,50))

# thima = lambda x:"Even" if x%2==0 else "Odd"
# # print(thima(10))
# # print(thima(11))



# ##############################################(upper)

# ding =lambda name :name .upper()
# print(ding("pavan"))


##################################################(txt file


###################################################