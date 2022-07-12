#Program to print union of two list 

def union(lst1,lst2):
    final_list = list(set(lst1) | set(lst2) )
    return final_list

n=int(input("Enter number of element for list1 :"))
lst1= []
for i in range (n):
    ele1=input("Enter element :")
    lst1.append(ele1)

m=int(input("Enter number of element for list2 :"))
lst2 = []
for i in range (m):
    ele2=input("enter element :") 
    lst2.append(ele2)

print(union(lst1,lst2))       
