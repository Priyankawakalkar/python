# 1.Write a Python program to get the frequency of the elements in a list.
list = []
no = int(input("Enter length of a list1 "))
print("Enter elements of list1 ")
for i in range(no):
 l1 = int(input())
 list.insert(i,l1)
print("List is =",list)
freq = {}
for item in list:
 if (item in freq):
 freq[item] += 1
 else:
 freq[item] = 1
for key, value in freq.items():
 print("%s : %d" % (key, value))

# 2.Write a program to check whether a list contains a sublist. 
list1 = []
no1 = int(input("Enter length of a list1 "))
print("Enter elements of list1 ")
for i in range(no1):
 l1 = int(input())
 list1.insert(i,l1)
print("List1 is =",list1)
list2 = []
no2 = int(input("Enter length of a sub-list "))
print("Enter elements of sub-list ")
for i in range(no2):
 l2 = int(input())
 list2.insert(i,l2)
print("sub-list is =",list2)
if (all(x in list1 for x in list2)):
 print("list contains a sublist")
else:
 print("list not contains a sublist")
Output:--
Enter length of a list1 5
Enter elements of list1
1
2
3
4
5
List1 is = [1, 2, 3, 4, 5]
Enter length of a sub-list 3
Enter elements of sub-list
1
4
5
sub-list is = [1, 4, 5]
list contains a sublist
