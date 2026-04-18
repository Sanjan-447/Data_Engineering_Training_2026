total=0
with open("data_1.txt", "r") as file:
    for line in file:
        total+=int(line.strip())  #convert txt to int and cancel spaces
print("Total : ", total)
