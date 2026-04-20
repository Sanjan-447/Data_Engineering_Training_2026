import json
#Task-18
students=[]
with open("marks.json", "r") as file:
    data=json.load(file)

students=data["students"]
marks=[]
for stu in students:
    marks.append(stu["marks"])

print("Highest marks: ", max(marks))
print("Lowest marks: ", min(marks))
print("Total marks: ", sum(marks))

#Task-19
courses=[]
for stu in students:
    # if stu["course"] not in courses:
    courses.append(stu["course"])
courses=tuple(courses)
print("Courses in tuple")
print(courses)

#Task-20
course_unique=set(courses)
print("Courses in set:")
print(course_unique)

#Task- 21
dict={}
for stu in students:
    dict[stu["name"]]= stu["marks"]
print("marks in dictionary:")
print(dict)

#Task-22
import csv
stud=[]
with open("attendance.csv", "r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        row["days_present"]=int(row["days_present"])
        row["total_days"] = int(row["total_days"]) 
        stud.append(row)

dict={}
for row in stud:
    dict[row["name"]]= (row["days_present"] / row["total_days"]) * 100
print("Dictionary with name and attendance percentage :")

print(dict)
