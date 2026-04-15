n=int(input("Enter a number: "))
fact=1
for i in range(n, 1, -1):
    fact=fact*i

print("Factorial: ", fact)
