numbers=[10,20,30,40,50]
#insertion
numbers.insert(2, 25)
print(numbers)

#remove
numbers.remove(40)
print(numbers)

#to remove last element
numbers.pop()
print(numbers)

#to find length
print(len(numbers))

for num  in numbers:
    print(num)

fruits=["apple","banana","mango"]
if "mango" in fruits:
    print("Mango exists")