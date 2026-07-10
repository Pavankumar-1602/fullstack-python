# def login(func):
#     def wrapper():
#         print("checking login")
#         func()
#     return wrapper
# @login
# def dashboard():
#     print("Dashboard page")
# dashboard()
#######################

# def message(func):
#     def wrapper():
#         print("functioin started")
#         func()
#         print("function ended")
#     return wrapper
# @message
# def hello():
#     print("hellow python")
# hello()

# def vinay():
#     print("vinay ia a boy")
# vinay()
############################

# import json

# student ={
#  "name ":"dinga",
#  "age":22
# }
# data=json.dumps(student)
# print(data)

##########################
import requests
response =requests.get(
    "https://api.github.com/users/python"
)
data=response.json()
print(data)