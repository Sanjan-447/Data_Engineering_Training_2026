l=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    e=int(input("Enter the element: "))
    l.append(e)

sum=0
for i in l:
    sum+=i

print("Sum of list : ", sum)