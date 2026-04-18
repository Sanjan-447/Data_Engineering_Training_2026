with open("logins.txt","r") as file:
    data=file.read().splitlines()

for name in data:
    print(name)

print("Total records : ",len(data))

count={}
for name in data:
    if name in count:
        count[name]+=1
    else:
        count[name]=1
print("no of times user logged in : ", count)
print("Maximum logged in user: ", max(count, key=count.get))
print("\n Unique users:")
for key in count.keys():
    print(key)