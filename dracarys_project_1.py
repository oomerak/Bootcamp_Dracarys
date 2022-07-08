
import pandas as pd
import numpy as np

student_number2 = []
first_name2 = []
last_name2 = []
points2 = []

#Define a function conv_grade
def conv_grade(points2):
    if points2 >=80 :
        return 'A'
    elif points2 >=70:
        return 'B'
    elif points2 >=60:
        return 'C'
    elif points2 >=50:
        return 'D'
    else:
        return 'F'


def situation2(point):
    if point<50:
        return "FAILED"
    else:
        return "PASSED"

#Check the func
#conv_grade(70)


#Define a function. That takes student name and points.
def message(student_number, first_name, last_name, points, lesson):
    print(f"Student number : {student_number}, {first_name} {last_name} scored {points}/100 points in {lesson} and got the letter '{conv_grade(points)}' ")


#Title for MATH lesson
print("Application for MATH Lesson \n-------------------\n")


input_choice = input("Do you want to enter student? You must enter only 'yes' or 'no' \n")
for i in input_choice:
    if input_choice == ("yes"):

        student_number = int(input("Please enter student's ID: "))
        first_name = input("Please enter student's first name: ")
        last_name = input("Please enter student's last name: ")
        point = int(input("Please enter student's point: "))

        lesson_grade = conv_grade(point)
        situation = situation2(point)
      
        newStudentData = first_name + "," + last_name + "," + str(student_number) + "," + str(point) + "," + lesson_grade + "," + situation + "\n"
        student_report_file = open("student_report.csv" , "a") # a: Writing to new line (end) | w: Deleting first line and writing the new value

        student_report_file.write(newStudentData)
        
        input_choice = input("Do you want to enter another student? 'yes' or 'no' \n ")
        
    else: 
        print("The dataframe of students are saved to student_report.csv file.\nDataframe has been converted to excel file.")
        break




    
"""
try:
    students_file = open("student_report.csv", 'r')
    print('There is an existing report card for this student')
except:
    students_file = open("student_report.csv", 'w')
    students_file.write(message(15, "Cagla", "Kamaci", 29, "English"))

students_file.close()
""" 
