import json 
import csv
#Task-26
def read_names():
    with open("students.txt", "r") as file:
        names=file.read().splitlines()

    return names

#Task-27
def load_marks():
    students=[]
    with open("marks.json", "r") as file:
        data=json.load(file)

    students=data["students"]
    return students

#task-28
def load_attendance():
    stud=[]
    with open("attendance.csv", "r") as file:
        reader=csv.DictReader(file)
        for row in reader:
            row["days_present"]=int(row["days_present"])
            row["total_days"] = int(row["total_days"]) 
            stud.append(row)
    return stud

#task-29
def avg_marks(students):
    total=0
    for stu in students:
        total+=stu["marks"]
    return total/len(students)

#task-30
def attendance_percentage(days_present, total_days):
    return (days_present/total_days)*100

#task-31
def topper(students):
    topper=max(students, key=lambda x:x["marks"])
    return topper

#task-32

def generate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"
    

names=read_names()
print("\nnames: ", names)

students = load_marks()
print("\nStudents with marks: ", students)

attendance= load_attendance()
print("\nAttendance data: ", attendance)

print("\nAverage marks: ", avg_marks(students))

print("\nAttendance Percentage :", attendance_percentage(22, 25), "%")

topper = topper(students)
print("\nTopper:", topper["name"], "-", topper["marks"])

print("\nGrades:")
for student in students:
    print(student["name"], ":", generate_grade(student["marks"]))