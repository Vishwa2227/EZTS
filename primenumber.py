n=int(input("enter prime number"))
flag=0
if n==0 or n==1:
     flag=1
for i in range(2,int(n/2)):
        if n%i==0:
            flag=1
            break
if flag==0:
         print("  prime")
            
else:
    print("Not a prime")