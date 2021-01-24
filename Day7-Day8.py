# 1) Write a Python program to get the frequency of the elements in a list.
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

# 2) Write a program to check whether a list contains a sublist. 
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

 3) Write a program to create dictionary and access all elements with keys and values
dict = {}
num = int(input("Enter dictionary element number:"))
for i in range(num):
 key = input("key\n")
 value = int(input("value\n"))
 dict[key] = value
print("Dictionary =",dict)
print("Accessing Elements from dictionary ")
for key in dict:
 print(key,dict[key])

4) Write a Program to sort (ascending and descending) a dictionary by value
Program:--
dict = eval(input("Enter dictionary "))
print("dictionary is =",dict)
key = input("key\n")
value = int(input("value\n"))
dict.update({key:value})
print("updated dictionary =",dict)

3.Write a Program to add a key to a dictionary.
Program:--
dict = eval(input("Enter dictionary "))
print("dictionary =",dict)
print("sorted dictionary by values =",sorted(dict.items(),key = lambda x:x[1]))
