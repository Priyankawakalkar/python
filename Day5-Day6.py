# 13) Write a program to generate all permutations of a list
def per(list):
 if len(list) == 0:
 return []
 elif len(list) == 1:
 return [list]
 else:
 l =[]
 for i in range(len(list)):
 a = list[i]
 ab = list[:i] + list[i + 1:]
 for x in per(ab):
 l.append([a] + x)
 return l
list1 = []
num = int(input("Enter length of a list ="))
print("Enter elements of list = ")
for i in range(num):
 list1.append(int(input()))
print("list=",list1)
d = list(list1)
print("All permutations of a list = ")
for p in per(d):
 print(p)

# 14)Write a program to get the difference between the two lists.
list1 = []
no1 = int(input("Enter length of a list1 "))
print("Enter elements of list1 ")
for i in range(no1):
 l1 = int(input())
 list1.insert(i,l1)
print("List1 is =",list1)
list2 = []
no2 = int(input("Enter length of a list2 "))
print("Enter elements of list2 ")
for i in range(no2):
 l2 = int(input())
 list2.insert(i,l2)
print("List2 is =",list2)
diff_l1_l2 = list(set(list1) - set(list2))
diff_l2_l1 = list(set(list2) - set(list1))
total_diff = diff_l1_l2 + diff_l2_l1
print("Diff between L1 and L2 is =",total_diff) 

# 15) Write a program to convert a list of characters into a string.
list = []
no = int(input("Enter length of a list "))
print("Enter elements of list ")
for i in range(no):
 l1 = str(input())
 list.insert(i,l1)
print("List of character is =",list)
nlist = ''.join(list)
print("String is =",nlist)
