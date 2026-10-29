n=(int(input("enter the numbber of values:")))
largest=int(input("enter number 1:"))
for i in range(2,n+1):
    num=int(input("enter number"+str(i)+":"))
    if num>largest:
        largest=num
print("largest number is:",largest)