#sagar Ahire
#Program to sort elements in Acending and Decending order

l = []
n = int(input("Enter number of elements in array:"));
for i in range(n) :
    element=int(input("Enter number in numerical form :"));
    l.append(element)

l.sort(reverse=False)
print("Array in ascending order is :",l)
l.sort(reverse=True)
print("Array in Decending order is :", l)

