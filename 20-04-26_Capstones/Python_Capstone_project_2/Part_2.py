import json
#Task-6
with open("marks.json", "r") as file:
    marks=json.load(file)

students=marks["students"]

#task-7
for stu in students:
    print("Name: ", stu["name"], "  Marks: ",stu["marks"])

#Task-8
highest= max(students, key= lambda x:x["marks"])
print("Student with  highest marks:")
print(highest["name"]," : ", highest["marks"])

#Task-9
lowest= min(students, key= lambda x:x["marks"])
print("Student with  lowest marks:")
print(lowest["name"]," : ", lowest["marks"])

#Task-10
total=0
for stu in students:
    total+=stu["marks"]
print("Average marks: ", total/len(students))

#Task-11
print("Students enrolled in python course :")
for stu in students:
    if stu["course"]=="Python":
        print(stu)

#Task-12
count_course={}
for stu in students:
    course = stu["course"]
    if course in count_course:
        count_course[course]+=1
    else:
        count_course[course]=1

print("No of students in each course:")
print(count_course)