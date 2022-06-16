print("Enter a number: ")
n=int(input())
sum=0
temp=n
while(n>0):
    sum+=(n%10)
    n=n//10
if(temp%sum == 0):
    print(temp,"is a Harshad Number")
else:
    print(temp,"is not a Harshad Number")