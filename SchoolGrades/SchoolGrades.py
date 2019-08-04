import pymongo
#-------------------------------------------------------------------------------
# Name:        SchoolGrades
# Purpose:
#
# Author:      iestyn
#
# Created:     04/08/2019
# Copyright:   (c) iestyn 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

def loopPrintMenu():
    print("----= Menu Options =----")
    print("Enter the number for option you want")
    print("1. Search for a Student")
    print("2. Enter a new student details")
    print("3. Enter grades for student")
    print("4. delete a student")
    print("5. Exit Program")

def mainMenu(integerInput):
    try:
        integerInput = int(integerInput)
    except ValueError:
        print("Please Enter the correct option")
        return None

    if(integerInput==1):
        searchStudent()
    elif(integerInput==2):
        enterStudent()
    elif(integerInput==3):
        enterGrades()
    elif(integerInput==4):
        deleteStudent()
    elif(integerInput==5):
        print("Exiting Program")
        quit()
    else:
        print("Please Enter the correct option")

def searchStudent():
    print("Search Student")

def enterStudent():
    print("Enter new student details")

def enterGrades():
    print("Enter student grades")

def deleteStudent():
    print("Enter studentID to be deleted")


while(True):
    loopPrintMenu()
    loopInput = input()
    mainMenu(loopInput)
