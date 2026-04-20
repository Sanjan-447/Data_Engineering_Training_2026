#Task-1

with open("website_visits.txt", "r") as file:
    visits=file.read().splitlines()

#Task-2
for i in visits:
    print(i)

#Task-3
print("Total no of visits: ", len(visits))

#Task-4
unique=set(visits)
for visit in unique:
    print(visit)

#Task-5
count={}
for name in visits:
    if name not in count:
        count[name] = 1
    else:
        count[name]+=1
print(count)
#Task-6
print("Most frequent visitor: ", max(count, key=count.get))
