#Program to check if the list contains 3 consecutive common numbers

l = []
n = int(input("Enter number of element in array :"));

for i in range(n):
    element=int(input("Enter elements :"))
    l.append(element)

key=l[0]
count=1 
for i in l[1::]:
    if key==i :
        count+=1
    else:
        count=1
        key=i
    if count>=3:
        print("YES,the given list contains three consecutive common numbers")
        break
else:
    print("NO, The list does not contains 3 consecutive common numbers")                