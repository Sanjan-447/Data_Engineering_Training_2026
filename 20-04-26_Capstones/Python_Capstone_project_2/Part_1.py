
with open("students.txt", "r") as file:
    names=file.read().splitlines()
    
#Task - 1
print("List of students:")    
print(names)

# Task-2
print("Total no of entries: ", len(names))

#Task-3
unique=set(names)
print("Unique names : ")
print(unique)

#Task-4
count={}
for name in names:
    if name not in count:
        count[name]=1
    else:
        count[name]+=1

print("No of times each student name appears: ",count)

#Task-5
with open("unique_students.txt", "w") as file:
    for name in unique:
        file.write(name+"\n")

print("\nUnique student names written into the unique_students.txt file")

