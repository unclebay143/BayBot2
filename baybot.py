# Programmer/developer:: Ayodele Samuel Adebayo
# ND1 semester1
# A program that interacts with the users
# d im user_talk,username,usermessage,confirm,baytalk
"""converting BASIC to PYTHON"""
import sys
import time
import datetime
import MySQLdb
developer = "Ayodele Samuel Adebayo"
developernickname = "UncleBigBay"
bot_name = "BAY-BOT"
print('')
print("Project By: " + developer)
print("Project Name:" + bot_name + "\n")
confirm = " "
name = " "

# CONNECTION TO baybotdb
db_conn = MySQLdb.connect(
    host="localhost",
    db="baybotdb",
    user="root",
    password=""
)


# Function for name/greeting animation
def animation(k):
    greet = ("\n Welcome " + k.upper() + "," + "\n\n what can I do for you?. (1 at a time?)\n")
    for i in range(len(greet)):
        time.sleep(0.1)
        sys.stdout.write("" + greet[i % len(greet)])
        sys.stdout.flush()


# Function that Gives My number
def menu2():
    print("\n07014525696 or 07087661935")
    bot_message = name.upper() + " took your number, did you received a call?"
    # saving message to notepad
    offlinemessage = open("offlinemessage.txt", "a")
    message_time = datetime.datetime.now()
    sendmakeup = ("\n\n\n" + "Name: " + bot_name + "\n" + "Message: " +
                  bot_message + "\n" + "Time: " + str(message_time.strftime("%c")))
    offlinemessage.write(sendmakeup)
    offlinemessage.close()

    # saving message to baybotdb
    cursor = db_conn.cursor()
    add_visitor_entry = ("INSERT INTO visitor"
                         "(visitor_name, message)"
                         "VALUES(%s, %s)")
    visitor_data_entry = (bot_name, bot_message)
    cursor.execute(add_visitor_entry, visitor_data_entry)
    db_conn.commit()
    cursor.close()
    db_conn.close()

    menu()


# Emergency number
def emergency():
    print("\nFor Emergency: Bay's Mom: 08038157444")
    menu()


# Menu3
def menu3():
    print("No Network Coverage.....Try using Your phone")
    menu2()


# Function for offline message from visitor stored in a txt file
def menu4():
    # saving message to notepad
    offlinemessage = open("offlinemessage.txt", "a")
    message_time = datetime.datetime.now()
    writemessage = (input("leave your message: "))
    sendmakeup = ("\n\n\n" + "Name: " + name + "\n" + "Message: " +
                  writemessage + "\n" + "Time: " + str(message_time.strftime("%c")))
    offlinemessage.write(sendmakeup)
    offlinemessage.close()
    process = " \nMessage Sent Successfully"
    for i in range(len(process)):
        time.sleep(0.1)
        sys.stdout.write("" + process[i % len(process)])
        sys.stdout.flush()

    # saving message to baybotdb
    cursor = db_conn.cursor()
    add_visitor_entry = ("INSERT INTO visitor"
                         "(visitor_name, message)"
                         "VALUES(%s, %s)")
    visitor_data_entry = (name, writemessage)
    cursor.execute(add_visitor_entry, visitor_data_entry)
    db_conn.commit()
    cursor.close()
    db_conn.close()
    returntomenu = "1"
    ask = input("\n Press 1 to return to menu: ")
    if ask == returntomenu:
        menu()
    else:
        print("Invalid Entry")
        nameattack()


# Def for Area Of A circle
def areaofacircle():
    radius = input(" Enter your radius to calculate the area:r = ")
    r = int(radius)
    r2 = int(r * r)
    pi = 3.143
    a = float(pi * r2)
    answer = str(a)
    print("\n\nThe area of a circle with radius " + radius + " is \n" + "= " + answer)
    pi = str(pi)
    radius = str(radius)
    r = str(r)
    explanation = (
            "\n\nThe formular for area of a circle is πr^2 \n\n We Should all know that π is equal to 22%7 = " + pi +
            " and your radius is " + r + " : - " + pi + " X" + radius + " = " + answer)
    print()
    print()
    print("\nShould I explain?.... Y/N")
    explain = input("\n")
    if explain.lower() == "y" or "yes":
        for i in range(len(explanation)):
            time.sleep(0.1)
            sys.stdout.write("" + explanation[i % len(explanation)])
            sys.stdout.flush()
    elif explain.lower() == "n" or "no":
        menu5()
    else:
        print("wrong input")
        menu5()


# Function to check user choice of math topic
def mathtopic(t):
    if t == 1:
        areaofacircle()
    else:
        print("coming soon!!!")


# Mathematics Function # MENU 5
def menu5():
    print("\nwelcome, What can i solve for you?")
    print(" 1. Area of a circle or About circle")
    print(" 2. Simple Addition")
    print(" 3. Meaning of BODMAS")
    topic = input("Select: ")
    mathtopic(topic)


# function for user request from the menu
def userrequest(n):
    if n < 1 or n > 7:
        print("Invalid Entry")
    elif n == 1:
        menu1()
    elif n == 2:
        menu2()
    elif n == 3:
        menu3()
    elif n == 4:
        menu4()
    elif n == 5:
        menu5()
    elif n == 6:
        emergency()
    elif n == 7:
        nameattack()
    else:
        print("smiles....bug everywhere")


# function for availability of the administrator
def menu1():
    print("Lemme check if he is around")
    # send a beep to my device to notify me about the visitor
    # notify bay(program in progress)
    time.sleep(5)
    print("Sorry..." + name.upper() + " he is not around")
    baybot_message = name.upper() + " ask of you. I said you weren't around"
    # saving message to baybotdb
    cursor = db_conn.cursor()
    add_baybot_entry = ("INSERT INTO visitor"
                        "(visitor_name, message)"
                        "VALUES(%s, %s)")
    baybot_data_entry = (bot_name, baybot_message)
    cursor.execute(add_baybot_entry, baybot_data_entry)
    db_conn.commit()
    cursor.close()
    db_conn.close()

    # saving message to notepad
    offlinemessage = open("offlinemessage.txt", "a")
    message_time = datetime.datetime.now()
    sendmakeup = ("\n\n\n" + "Name: " + bot_name + "\n" + "Message: " +
                  baybot_message + "\n" + "Time: " + str(message_time.strftime("%c")))
    offlinemessage.write(sendmakeup)
    offlinemessage.close()

    menu()


# User menu
def menu():
    animation(name)
    # print("")
    time.sleep(0.2)
    print("\n" + " 1. I want to see " + developer.upper() + "\n")
    time.sleep(0.2)
    print(" 2. I need BigBay's Number" + "\n")
    time.sleep(0.2)
    print(" 3. Put a call through to BigBay" + "\n")
    time.sleep(0.2)
    print(" 4. I want to leave a message for him" + "\n")
    time.sleep(0.2)
    print(" 5. Do some mathematics" + "\n")
    time.sleep(0.2)
    print(" 6. Emergency Number" + "\n")
    print(" 7. Return")
    usermenu = int(input("\nEnter: "))
    userrequest(usermenu)


# admin menu
def adminmenu():
    print("Welcome Programmer " + developernickname.upper())
    print(" ")
    print("1.Show Messages\n")
    print("2.number of visitors\n")


# function for security check into adminmenu
def detector(m):
    code = "yes"
    if m == code:
        print("\nPassed \n")
        adminmenu()
    else:
        print("\nAccess Denied \n")
        menu()


# check if name Boss or visitor
def checkboss(n):
    db = "bigbay"
    if n.lower() == db or n.lower() == "bayo":
        print("\n Is that you boss? ")
        yesorno = input(" \n")
        if yesorno == "yes":
            print("\n Confirm Identity")
            confirm_identity = input(" \n")
            detector(confirm_identity)
        else:
            animation(n)
            menu()
    else:
        menu()


# Ask name of the visitor
def nameattack():
    global name
    print("\nHi, I am BayBot \n ")
    name = input("What is your name? ")
    if name == "":
        print("\nAnonymous not allowed..Anonymous is a name too")
        nameattack()
    else:
        checkboss(name)


# program start
nameattack()
