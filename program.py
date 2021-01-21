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

# 7)Write a program to count the number of strings where the string length is 2 or more and the first
and last character are same from a given list of strings.
Program :--
list = []
num = int(input("Enter length of a list "))
print("Enter elements of list ")
count = 0
for i in range(num):
 l1 = (input())
 list += [l1]
 if len(l1) > 1 and l1[0] == l1[-1]:
 count = count + 1
print("list =",list)
print("number of strings having same first and last character = ",count)
Output:--
Enter length of a list 5
Enter elements of list
123
121
zpz
anu
525
list = ['123', '121', 'zpz', 'anu', '525']
number of strings having same first and last character = 3 

# 8)Write a program to get a list, sorted in increasing order by the last element in each tuple from a
given list of non-empty tuples.
Program:--
def last(n):
 return n[-1]
def sorted_list(tuples):
 return sorted(tuples, key=last)
list = []
l1 = ((input("Enter list of tuples \n")))
while (l1 != ''):
 list.append(tuple(map(int, l1.split())))
 l1 = input()
print("list =",list)
print("The Sorted list is =",sorted_list(list))
Output:--
Enter list of tuples
1 5
2 3
9 8
6 5
7 0
list = [(1, 5), (2, 3), (9, 8), (6, 5), (7, 0)]
The Sorted list is = [(7, 0), (2, 3), (1, 5), (6, 5), (9, 8)] 

# 9)Write a program to remove duplicates elements from a list.
Program:--
list = []
no = int(input("Enter the length of a list "))
print("Enter elements of list ")
for i in range(no):
 list.append(int(input()))
print("list = ", list)
list1= []
for element in list:
 if element not in list1:
 list1.append(element)
print("list without duplicates =",list1)
Output:--
Enter the length of a list 5
Enter elements of list
23
56
89
23
56
list = [23, 56, 89, 23, 56]
list without duplicates = [23, 56, 89] 
