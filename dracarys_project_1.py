import pandas as pd
import numpy as np


# Grade Result Function
def grade_func(points2):
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

# Status Result
def situation2(point):
    if point<50:
        return "FAILED"
    else:
        return "PASSED"

# We dont want to numbers in input values 
def checkStrings(name):
    if any(chr.isdigit() for chr in name) == True:
        raise InvalidValueInStrıngError
    else:
        pass

# Is point between 0 and 100?
def pointValueCheck(pts):
    if 0<=pts<=100:
        pass
    else:
        raise PointValueCheckError

# We made this for catch numbers in strings
class InvalidValueInStrıngError(ValueError):
    pass

#Checking point and getting error when point is lower than 0 and bigger than 100
class PointValueCheckError(ValueError):
    pass

#DATA dict of Students
data = {}

#Column List for Student Amount  
column = []


#Title for MATH lesson
print("Application for MATH Lesson \n-------------------------------\n")


process2 = True

# For Getting Student(s) Amount From User
while process2 == True:
    try:
        studentamount = int(input("Please enter number of students\n----------\n"))

    except ValueError:
        process2 = True

    else:
        process2 = False



for i in range (studentamount):
    process = True

    while process == True:
        try:
            print(f"STUDENT {i+1}: ")
            student_number = int(input("\nPlease enter student's ID: "))
            first_name = input("Please enter student's first name: ")
            checkStrings(first_name)    
            last_name = input("Please enter student's last name: ")
            checkStrings(last_name)
            point = int(input("Please enter student's point: "))
            pointValueCheck(point)        

        except PointValueCheckError:
            print("---\nYour exam point must be between 0 and 100 !\n---\n")
            process = True
    
        except InvalidValueInStrıngError:
            print("---\nYou can't enter any number in first and last name!\n---\n")
            process = True

        except TypeError:
            print('Oh no! A TypeError has occured')
            process = True


        except ValueError:
            print('A ValueError occured!\n-----\n')
            process = True


        else:
            print(f'Student {i+1} is Saved.\n')
            process = False

   

    if process == False:
        lesson_grade = grade_func(point)
        situation = situation2(point)

        #Four column name
        aboutstudent = str("Student " + str(i+1))
        column.append(aboutstudent)

        newDict = {aboutstudent : [first_name,last_name,student_number,point,lesson_grade,situation]}
        data.update(newDict)

       

df = pd.DataFrame.from_dict(data , orient="index" , columns=["First Name","Last_name","Student Number","Point", "Grade" , "Status"])
print(df)      
print("---------- --------")
writer = pd.ExcelWriter('Lesson Report.xlsx')
df.to_excel(writer)
writer.save()
print("\nDataframe has been converted to excel file.")
print("---------- END --------")


