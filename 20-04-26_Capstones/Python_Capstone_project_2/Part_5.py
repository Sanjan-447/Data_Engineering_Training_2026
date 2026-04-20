import json
students=[]
with open("marks.json", "r") as file:
    data=json.load(file)

students=data["students"]


import csv 
stud=[]
with open("attendance.csv", "r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        row["days_present"]=int(row["days_present"])
        row["total_days"] = int(row["total_days"]) 
        stud.append(row)
#task-23
print("Pass or Fail")
for stu in students:
    if stu["marks"] >= 50:
        print(stu['name'], " : Pass" )
    else:
        (stu['name'], " : Fail" )

#Task-24
print("Students with grades")
for stu in students:
    if stu["marks"] >=90:
        print(stu["name"], ": A")
    elif stu["marks"] >= 75:
        print(stu["name"], ": B")
    elif stu["marks"] >= 50:
        print(stu["name"], ": C")
    else:
        print(stu["name"], ": Fail")

#Task-25
print("students with marks above 80")
for stu in students:
    if stu["marks"] > 80:
        print(stu["name"], " : ", stu["marks"])
    
print("students with attendance above 85")
for stu in stud:
    if ((stu["days_present"]/ stu["total_days"]) *100) > 85:
        print(stu["name"])

