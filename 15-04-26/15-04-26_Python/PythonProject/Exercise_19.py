l=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    e=int(input("Enter the element: "))
    l.append(e)

small=l[0]
for i in l:
    if i < small:
        small=i
print("Minimum element is: ", small)