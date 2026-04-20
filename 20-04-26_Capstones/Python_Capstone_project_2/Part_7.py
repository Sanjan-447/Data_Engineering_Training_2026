import json
import csv

def generate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

with open("marks.json", "r") as file:
    data = json.load(file)

students = data["students"]

attendance_dict = {}

with open("attendance.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["name"]
        days_present = int(row["days_present"])
        total_days = int(row["total_days"])

        attendance_percentage = (days_present / total_days) * 100
        attendance_dict[name] = attendance_percentage

#Task-33

combined_data = {}

for student in students:
    name = student["name"]
    marks = student["marks"]

    combined_data[name] = {
        "marks": marks,
        "attendance": attendance_dict.get(name, 0),
        "course": student["course"],
        "grade": generate_grade(marks)
    }

print(combined_data)

#Task-34
for name, info in combined_data.items():
    print("Name : ", name)
    print("Marks: ", info["marks"])
    print('Attendance : ',info["attendance"])
    print("Course : ", info["course"])
    print("Grade : ", info["grade"])
    print()

#Task-35
print("Students eligible for certification")
for name,info in combined_data.items():
    if info["marks"] >= 75 and info["attendance"] >= 80:
        print(name)

#Task-36
print("Students who need imporvement: ")
for name, info in combined_data.items():
    if info["marks"] < 75 or info["attendance"] < 80:
        print(name)