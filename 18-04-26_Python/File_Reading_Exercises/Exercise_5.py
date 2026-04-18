import csv

employees=[]
with open("employees.csv", "r") as file:
     reader=csv.DictReader(file)
     for row in reader:
         row["salary"]=int(row["salary"])
         employees.append(row)

for emp in employees:
    print(emp["name"])

emps={}
print("employees working in IT dept:" )
for emp in employees:
   if emp["department"] == "IT" :
          emps[emp["name"]] = emp["department"]
   else:
       pass
print(emps)
total_sal=0
for emp in employees:
   total_sal += emp["salary"]
avg_sal=total_sal/len(employees)
print("Average salary: ", avg_sal)

highest=max(employees, key=lambda x:x["salary"])
print("Highest salary employees:")
print(highest["name"], "-", highest["salary"])

dept_count={}
for emp in employees:
   dept=emp["department"]
   if dept in dept_count:
       dept_count[dept]+=1
   else:
       dept_count[dept]=1
print("Employees in each dept: ")
print(dept_count)
