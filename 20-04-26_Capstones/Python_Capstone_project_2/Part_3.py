import csv
#Task-13
students=[]
with open("attendance.csv", "r") as file:
    reader=csv.DictReader(file)

    for row in reader:
        row["days_present"]=int(row["days_present"])
        row["total_days"] = int(row["total_days"]) 
        students.append(row)

#task-14
print("Attendance details:")
for student in students:
    print(student["name"], "-", student["days_present"], "-", student["total_days"])

#Task-15
print("Attedance percentage details")
for student in students:
    percentage = (student["days_present"] / student["total_days"]) * 100
    student["percentage"] = percentage
    print(student["name"], ":", percentage, "%")

#Task -16
print("Students having attendance less than 80")
for student in students:
    if student["percentage"] < 80:
        print(student["name"], "-", student["percentage"], "%")

#Task - 17
print("Student with best attendance")
highest=max(students, key=lambda x:x["percentage"])
print(highest["name"], " - ", highest["percentage"])
