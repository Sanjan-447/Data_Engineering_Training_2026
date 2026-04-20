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


def load_marks():
    with open("marks.json", "r") as file:
        data = json.load(file)
    return data["students"]


def load_attendance():
    attendance_dict = {}

    with open("attendance.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row["name"]
            days_present = int(row["days_present"])
            total_days = int(row["total_days"])

            percentage = (days_present / total_days) * 100
            attendance_dict[name] = percentage

    return attendance_dict


def combine_data(students, attendance_dict):
    combined_data = {}

    for student in students:
        name = student["name"]
        marks = student["marks"]
        attendance = attendance_dict.get(name, 0)

        combined_data[name] = {
            "marks": marks,
            "attendance": attendance,
            "course": student["course"],
            "grade": generate_grade(marks)
        }

    return combined_data


def find_topper(combined_data):
    return max(combined_data, key=lambda name: combined_data[name]["marks"])

def find_best_attendance(combined_data):
    return max(combined_data, key=lambda name: combined_data[name]["attendance"])

def avg_marks(combined_data):
    total=0
    for value in combined_data.values():
        total+=value["marks"]
    return total/len(combined_data)

def eligible_students(combined_data):
    eligible=[]
    for name,info in combined_data.items():
        if info["marks"] >= 75 and info["attendance"] >= 80:
            eligible.append(name)
    return eligible

def improvement_students(combined_data):
    improve = []
    for name, info in combined_data.items():
        if info["marks"] < 75 or info["attendance"] < 80:
            improve.append(name)
    return improve

students = load_marks()
attendance_dict = load_attendance()

combined_data = combine_data(students, attendance_dict)

topper = find_topper(combined_data)
best_att = find_best_attendance(combined_data)
avg_marks = avg_marks(combined_data)

eligible_list = eligible_students(combined_data)
improve_list = improvement_students(combined_data)
#Task - 39, 40
print("Topper:", topper)
print("Best Attendance:", best_att)
print("Average Marks:", round(avg_marks, 1))
print("Eligible Students:", ", ".join(eligible_list))
print("Students Needing Improvement:", ", ".join(improve_list))