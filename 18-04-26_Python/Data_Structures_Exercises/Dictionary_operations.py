student={
    "name" : "Arjun",
    "age" : 25,
    "course":"Python"
}

print(student)

#getting values using keys
print(student["name"])
print(student["age"])
print(student["course"])

#get
print(student.get("name"))
print(student.get("age"))

#add a new pair
student["city"]= "Hyderabad"
print(student)