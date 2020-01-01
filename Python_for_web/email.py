import time     
from db import list_users 
from db import query_user_last_seen, list_users
from datetime import datetime as dt, timedelta


registered_users = list_users() 
date = dt.now()

def if_exist(user_name):
    i = 0 
    while i < len(registered_users):     
        username = registered_users[i][0]         
        if username == user_name:
            return True
        i -= -1
    return False

user_email = ''
user_login = ''
attemps = 3

def login():
    user_email = input("Enter email: ")
    user_login = user_email.split("@")[0].lower()
    attemps = 3
    while if_exist(user_login) != 1 and attemps > 0:
        print("User " + user_login + " dont exist. Please retype your email!")
        user_email = input(str(attemps) + "| " + "Enter email: ")
        user_login = user_email.split("@")[0].lower()
        attemps +=- 1
    if if_exist(user_login):
        return 1
    else:
        return 0


login()

while login() != 1:
    print("Because you has entered incorect password more that " + str(attemps) + " dates, acces has been blocked for 15 sec")
    time.sleep(15)
    

i = 0 
while i < len(registered_users):     
    username = registered_users[i][0]     
    last_seen = registered_users[i][1]    
    i -= -1
    if username == user_login:
        date = last_seen
        

from_last_seen = dt.now() - dt(year=date.year, month=date.month, day=date.day)
valid_date = dt.now() + timedelta(days=360)

if from_last_seen.days > 360:
    print("From last seen it's been more than 360 days")
    print("You need to recomfirm your account")
else:
    print("Your account is valid until " + str(valid_date.year) + "-" + str(valid_date.month) + "-" + str(valid_date.day))

