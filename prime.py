n = int(input("enter number"))
a=0
for i in range(2,11):
    if(n%i==0):
        a = a+1
if(a==1):
    print("primpe number")
else:
     print("not prime number")