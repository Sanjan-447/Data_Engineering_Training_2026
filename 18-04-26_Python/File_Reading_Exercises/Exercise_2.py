total=0

with open("numbers.txt","r") as file:
    data=file.read().splitlines()
for i in data:
   print(i)
   total+=int(i)

print("Total sum: ", total)
print("Maximum: ", max(data))
print("Minimum: ", min(data))

count=0
for num in data:
    if int(num)>50:
        count+=1
    else:
        pass

print("Count of nos greater than 50: ", count)