l=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    e=int(input("Enter the element: "))
    l.append(e)

mx=l[0]
for i in l:
    if i > mx:
        mx=i
print("Maximum element is: ", mx)