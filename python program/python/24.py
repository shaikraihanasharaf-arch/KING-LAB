n=int(input())
i=1
sum=0
while i<=n:
    if i%2==0:
        sum+=i
    i+=1
print(f" the sum of even numbers up to {n} is:", sum)
