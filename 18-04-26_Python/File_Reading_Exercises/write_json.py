import json

students= { "students" : [
    {"name" : "Priya", "marks" :88},
    {"name" : "Karan", "marks": 98}
]}

with open("output.json", "w") as file:
    json.dump(students, file , indent=3) # it will indent the data accordingly
                                         # will make the data presentable
