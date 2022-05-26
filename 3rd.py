n=int(input())
a=int(input())
b=int(input())
k=0
for i in range (1, n+1):
    if i%a==0:
      k+=1
    if i%a!=0 and i%b==0:
      k+=1  
print(k)