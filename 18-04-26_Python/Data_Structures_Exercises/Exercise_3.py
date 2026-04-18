students = {
"Rahul":85,
"Sneha":92,
"Arjun":78,
"Priya":88
}

print("Topper: ", max(students, key=students.get))

avg=sum(students.values())/len(students)
print("average marks: ",avg)

print("student scoring above 85")
for name,marks in students.items():
    if marks > 85:
        print(name , " : ",marks )