n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
for j in range(n1,n2+1,1):    
    for i in range(1,11,1):        
        print(j,i,i*j)
    print()
