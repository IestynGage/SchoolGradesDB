import pymongo
from pymongo import MongoClient
#-------------------------------------------------------------------------------
# Name:        SchoolGrades
# Purpose:     To have a command line menu that can interact with MongoDB
#
# Author:      iestyn
#
# Created:     04/08/2019
# Copyright:   (c) iestyn 2019
# Licence:     MIT
#-------------------------------------------------------------------------------

cluster = MongoClient("mongodb+srv://user:123@cluster0-inbbm.mongodb.net/test?retryWrites=true&w=majority")
db = cluster["school"]
collection = db["students"]

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
        id = input("Enter student ID")
        searchStudent(int(id))
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

def searchStudent(id):
    results = collection.find({"_id":id})
    for result in results:
        print(result)

def enterStudent():
    FName = input("Please enter students First Name")
    LName = input("Please enter students Last Name")
    student = {"FName":FName,"LName":LName}

    collection.insert_one(student)

def enterGrades():
    print("Enter student grades")

def deleteStudent():
    studentID = input("Please enter students ID to be deleted")
    deleteQuery = {"_id":studentID}
    collection.delete_one(deleteQuery)

while(True):
    loopPrintMenu()
    loopInput = input()
    mainMenu(loopInput)


