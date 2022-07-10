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


#Define a function. That takes student name and points.
def message(student_number, first_name, last_name, points, lesson):
    print(f"Student number : {student_number}, {first_name} {last_name} scored {points}/100 points in {lesson} and got the letter '{conv_grade(points)}' ")


#Converting the Dataframe(csv) file to excel (xlsx) file

def convert2Excel1():

    df = pd.read(r"student_report.csv")
    c2e = df.to_excel(r"student_report.xlsx" , index = None , header = False)




    

#Title for MATH lesson
print("Application for MATH Lesson \n-------------------------------\n")


process2 = True


while process2 == True:
    try:
        studentamount = int(input("Please enter number of students\n"))

    except ValueError:
        process2 = True

    else:
        process2 = False


for i in range (studentamount):
    process = True

    while process == True:
        try:
            student_number = int(input("Please enter student's ID: "))
            first_name = input("Please enter student's first name: ")
            last_name = input("Please enter student's last name: ")
            point = int(input("Please enter student's point: "))

            
        except TypeError:
            print('Oh no! A TypeError has occured')
            process = True

        except ValueError:
            print('A ValueError occured!')
            process = True

        else:
            print('No exception')
            process = False

    
    if process == False:
        lesson_grade = conv_grade(point)
        situation = situation2(point)

        newStudentData = first_name + "," + last_name + "," + str(student_number) + "," + str(point) + "," + lesson_grade + "," + situation + "\n"

        
        student_report_file = open("student_report.csv" , "a") # a: Writing to new line (end) | w: Deleting first line and writing the new value

        student_report_file.write(newStudentData)
    



df = pd.read_csv(r"student_report.csv")
writer = pd.ExcelWriter('Proje1.xlsx')
df.to_excel(writer)
 
writer.save()


print("The dataframe of students are saved to student_report.csv file.\nDataframe has been converted to excel file.")
