#Program to print Transpose of matrix

R = int(input("Enter the number of rows :"))
C = int(input("Enter the number of columns :"))

A = []
print("Enter the entries rowwise :")

for i in range(R):
    a = []
    for j in range(C):
        a = []
        for j in range(C):
            a.append(int(input()))
    A.append(a)

print("The matrix A is :")
for i in range(R):
    for j in range(C):
        print(A[i][j], end = "")
    print()

    print("The transpose of matrix A is :")
    for i in range (R):
        print(A[j][i], end = "")
    print()    