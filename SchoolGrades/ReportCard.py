from fpdf import FPDF
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      iesty
#
# Created:     09/08/2019
# Copyright:   (c) iesty 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class ReportCard():
    studentName = None
    grades = []

    def addStudentName(self,name):
        self.studentName = name

    def addGrade(self,subject,grade):
        self.grades.append((subject,grade))

    def removeGrade(self,subject):
        for i in self.grades:
            if(i[0]==subject):
                self.grades.remove(i)
                break

    def printGrades(self):
        for subject in self.grades:
            print(subject)

    def generatePDF(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', '', 16)
        height = 40
        for grade in self.grades:
            pdf.cell(1, 0, grade[0] + " " + grade[1],0,2,'L')
            height+=20
        pdf.output(self.studentName +'.pdf', 'F')



rc = ReportCard()

rc.addStudentName("Iestyn")
rc.addGrade("Maths","E")
rc.addGrade("English","C")
rc.addGrade("Cat","A")
rc.printGrades()
rc.printGrades()
rc.generatePDF()