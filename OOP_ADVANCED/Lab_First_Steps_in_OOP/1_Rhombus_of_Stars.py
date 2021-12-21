def rhombus(n, j):
    for i in range(n-j):
        print(" ", end="")
    for p in range(j):
        print("*", end=" ")


n = int(input())

for j in range(1, n+1):
    rhombus(n, j)
    print()
for j in range(n-1, 0, -1):
    rhombus(n, j)
    print()