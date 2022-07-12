#python program to extract elements with frequency greater than k

list1 = []
n=int(input("Enter no of elements in a list :"));

for i in range(n):
    element=int(input("Enter elements :"))
    list1.append(element)

k=int(input("Enter value of k :"))

list2=[]
for i in range (n):
    if list1[i]>k:
        list2.append(list1[i])

print("Elements with frequency greater than ",k,"are:")        

length=len(list2)
for i in range (length):
    print(list2[i])