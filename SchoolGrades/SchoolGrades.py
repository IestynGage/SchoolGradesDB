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

cluster = MongoClient()
db = cluster["school"]
collection = db["students"]

def loopPrintMenu():
    '''
    This prints all the options thar are possible
    '''
    print("----= Menu Options =----")
    print("Enter the number for option you want")
    print("1. Search for a Student")
    print("2. Enter a new student details")
    print("3. Enter grades for student")
    print("4. delete a student")
    print("5. print all students")
    print("6. Exit Program")

def mainMenu(integerInput):
    '''
    This takes input and calls function to said integer
    '''
    try:
        integerInput = int(integerInput)
    except ValueError:
        print("Please Enter the correct option")
        return None

    switcher = {
        1:searchStudent,
        2:enterStudent,
        3:enterGrades,
        4:deleteStudent,
        5:printAllStudents,
        6:quitprogram
    }

    function = switcher.get(integerInput,lambda: print("Please Enter the correct option"))

    function()

def searchStudent():
    id = input("Enter student ID")
    results = collection.find({"_id":int(id)})
    for result in results:
        print(result)

def enterStudent():
    FName = input("Please enter students First Name")
    LName = input("Please enter students Last Name")
    student = {"_id":collection.count()+1,"FName":FName,"LName":LName}

    collection.insert_one(student)

def enterGrades():
    studentID = input("Please Enter students ID")
    subject = input("Please enter students subject")
    grade = input("Please enter students grade for " + subject)

    query = {"_id":int(studentID)}
    newValue = { "$set": {subject : grade}}

    collection.update_one(query,newValue)

def deleteStudent():
    studentID = input("Please enter students ID to be deleted")
    deleteQuery = {"_id":int(studentID)}
    x = collection.delete_one(deleteQuery)
    print(x.deleted_count, "documents deleted.")

def printAllStudents():
    results = collection.find()
    for result in results:
        print(result)

def quitprogram():
    print("Exiting Program")
    quit()

while(True):
    loopPrintMenu()
    loopInput = input()
    mainMenu(loopInput)


