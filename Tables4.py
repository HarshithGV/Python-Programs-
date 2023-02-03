f1=open("in1.txt","r")
f2=open("out1.txt","w")
n1=int(f1.readline())
n2=int(f1.readline())
for j in range(n1,n2+1,1):    
    for i in range(1,11,1):        
        info1=str(j)+" "+str(i)+" "+str(i*j)
        print(info1)
        f2.write(info1)
        f2.write("\n")
    print()
    f2.write("\n")
f2.close()
