n=5
for i in range(1,n+1):
    for j in range(1,2*i,2):
        print(j,end=" ")
    for j in range(2*(n-i)):
        print(" ",end=" ")
    for j in range(2*i,1,-2):
        print(j,end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(1,2*i,2):
        print(j,end=" ")
    for j in range(2*(n-i)):
        print(" ",end=" ")
    for j in range(2*i,1,-2):
        print(j,end=" ")
    print()