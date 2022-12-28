R=int(input("Enter The Number of rows:"))
C=int(input("Enter The Number of Columns:"))
matrix=[]
print("Enter the entries row wise:")
for i in range(R):
    a=[]
    for j in range(C):
        a.append(int(input()))
    matrix.append(a)

print("Matrix is:",end=" \n")
for i in range(R):
    for j in range(C):
       print(matrix[i][j],end=" ")
    print()


R=int(input("Enter The Number of rows:"))
C=int(input("Enter The Number of Columns:"))
matrix1=[]
print("Enter the entries row wise:")
for i in range(R):
    b=[]
    for j in range(C):
        b.append(int(input()))
    matrix1.append(b)

print("Matrix is:",end=" \n")
for i in range(R):
    for j in range(C):
      print(matrix1[i][j],end=" ")
    print()

print("Addition :",end=" \n")
for i in range(R):
    for j in range(C):
       print(matrix1[i][j]+matrix[i][j],end=" ")
    print()

print("Subtraction :",end=" \n")
for i in range(R):
    for j in range(C):
       print(matrix1[i][j]-matrix[i][j],end=" ")
    print()


print("Transpose:",end=" \n")
for i in range(R):
    for j in range(C):
       print(matrix[j][i],end=" ")
    print()


result=[[0 for i in range(C)] for i in range(R)]
for i in range(len(matrix)):
    for j in range(len(matrix1[0])):
        for k in range(len(matrix1)):
            result [i][j]+=matrix[i][k]*matrix1[k][j]
print("\nMultiplication is: ")
for r in result:
    print(r)

