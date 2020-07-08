import math
import random
n=int(input('Give the size of the matrix n by n >>>>>>    n = '))
print(n)
print()
a = [[[] for i in range(0,n)] for j in range(0,n)]
b = [[random.randint(1,49) for i in range(0,n)]
     for j in range(0,n)]
for i in range(0,n):
    for j in range(0,n):
        a[i][j]=b[i][j]
        print(f'{str(a[i][j]):>4}', end=' ')
    print()
    print()
print()
print('After rotation clockwise 90 degrees')
print ()
for i in range(0,n):
    for j in range(0,n):
        a[i][j]=b[n-j-1][i]
        print(f'{str(a[i][j]):>4}', end=' ')
    print()
    print()
