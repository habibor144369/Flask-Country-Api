n1 = int(input("enter a first number:"))
n2 = int(input("enter a second number: "))

lis = []
for x in range(n1, n2 + 1):
    print(x)
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                break
        else:
            lis.append(x)
print(lis)


