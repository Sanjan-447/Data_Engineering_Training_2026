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

combined_data={}

for student in students:
    name=student["name"]
    marks=student["marks"]
    attendance= attendance_dict[name]
    grade=generate_grade(marks)

    combined_data[name]={
        "marks":marks,
        "attendance":attendance,
        "course":student["course"],
        "grade":grade 
    }

#Task-37
with open("report.txt","w") as file:
    file.write("Student Report\n")

    for name, info in combined_data.items():
        file.write(f"{name} - Marks: {info["marks"]} - Attendance: {info["attendance"]}% - Grade: {info["grade"]}\n")

print("Report written to report.txt")

#Task-38
with open("eligible_students.txt","w") as file:
    file.write("Eligible students\n")

    for name, info in combined_data.items():
        if info["marks"] >= 75 and info["attendance"] >= 80:
            file.write(f"{name}\n")

    print("Eligible students written to eligible_students.txt")
    