n=int(input())
if n>1:
    for i in range(2,5):
        if n%i==0:
            print("not a prime number")
            break
        else:
            print("prime number")
            break
else:
    print("not a prime")            
    
     