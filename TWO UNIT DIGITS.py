a,b=map(int,input("enter :").split())
c=a%10
d=b%10
if(c > d):
    for i in reversed(range(d,c+1)):
        print(i,end=" ")
else:
    for i in range(c,d+1):
        print(i,end=" ")
