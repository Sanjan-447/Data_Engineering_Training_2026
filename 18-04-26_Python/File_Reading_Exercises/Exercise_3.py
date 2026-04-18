import json

with open("students.json","r") as file:
    data=json.load(file)

print("names of students:")
for row in data["students"]:
    print(row["name"])

print("Students enrolled in Python course: ")
for row in data["students"]:
    if row["course"]=="Python":
        print(row)
    else:
        pass

highest_student = max(data["students"], key=lambda x: x["marks"])
print("\nStudent with highest marks:")
print(highest_student["name"], "-", highest_student["marks"])

total=0
for row in data["students"]:
     total+=row["marks"]
avg= total/len(data["students"])
print("Average marks: ",avg)

course_count={}
for row in data["students"]:
     course=row["course"]
     if course in course_count:
          course_count[course]+=1
     else:
          course_count[course]=1
print("Students enrolled in each course: ")
print(course_count)