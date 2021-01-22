# 1)Create List and Displayed with append() and without append()
print("using append() method")
list = []
n = int(input("Enter number of elements in the list : "))
for i in range(0, n):
   print("Enter element No.: ".format(i+1))
   elm = int(input())
   list.append(elm)
print("The entered list is: \n",list)
print("without using append() method")
p = ['a',1,2]
q = p + ["abc"]
print("list:",p)
print("new list:",q)

# 2)Add element at first, last and specific location in list
list =['2','3','priyanka','jui','durwa','kavita']
print("given list =", list)
print("add element at first location")
list.insert(0,"sonal")
print(list)
print("add element at specific location")
list1 = ['2','3','priyanka','jui','durwa','kavita']
list1.insert(2,"shubhangi")
print(list1)
list2 = ['2','3','priyanka','jui','durwa','kavita']
print("add element at last location")
list2.append("anuja")
print(list2)


# 3)Remove element from first position,last position and specific position from list
l1 = [11,'priyanka',54,'a',20]
print("given list =",l1)
print("Remove element form first position")
l1.remove(l1[0])
print(l1)
print("Remove element form specific position")
l2 = [11,'priyanka',54,'a',20]
l2.remove(l2[3])
print(l2)
print("Remove element form last position")
l3 = [11,'priyanka',54,'a',20]
l3.remove(l3[-1])
print(l3)

# 4)Write a Python program to create an list without append() display the list items. Access individual element through indexes.(get input from user)
list = []
no = int(input("Enter length of a list "))
print("Enter elements of list ")
for i in range(no):
 l1 = int(input())
 list.insert(i,l1)
print("Entered list =",list)
print("display list items ")
for i in list:
 print(i)
print("Access individual element of list through indexes ")
for i in range(len(list)):
 print(list[i])

# 5)Write a program to get the number of occurrences of a specified element in an list.
def count(list, x):
 c= 0
 for i in list:
 if (i == x):
 c = c + 1
 return c
list = []
num = int(input("Enter length of a list "))
print("Enter elements of list")
for i in range(num):
 l1 = int(input())
 list.insert(i,l1)
print("entered list =",list)
x = int(input("Enter specific element which is present in the list:"))
print("specified element:",x)
print("Occurrence of specified element in a list ")
print("{} occurred {} times in a list".format(x, count(list, x)))
 
# 6)Write a program to remove the first occurrence of a specified element from an list.
list = []
num = int(input("Enter length of a list: "))
print("Enter elements of list ")
for i in range(num):
 l1 = int(input())
 list.insert(i,l1)
print("entered list =",list)
x = int(input("Enter specific element which is present in the list "))
print("specified element:",x)
print("Remove the first occurrence of a specified element from list ")
list.remove(x)
print("New list = ",list)

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
