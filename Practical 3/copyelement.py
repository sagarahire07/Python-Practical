#Sagar ahire
#Program to copy elements of one array into another

arr1 = []
n = int(input("Enter the number of elements in array : "));

for i in range(n):
    element=int(input("Enter the element in numerical form 3: "))
    arr1.append(element)

arr2 =[]
for i in range(n):
    arr2.append(arr1[i])

print("The element of arr2 is :",arr2)