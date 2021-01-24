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

# 3.Write a program to check whether a list contains a sublist. 
