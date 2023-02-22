A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

print(((A+B)%C)\n((A%C)+(B%C)%C))
print((A*B)%C)
print(((A%C)*(B%C))%C)

A,B,C = map(int,input().split())

print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep='\n')
# sep='\n'로 줄바꿈