#program to print array element in reverse order 

arr = []
n=int(input("Enter the number of element in array :"));

for i in range(n):
    element=int(input("Enter element in numerical form :"))
    arr.append(element)

print("The elements in reverse are :")
for i in range(-1, -n-1 , -1):
    print(arr[i])