# 7)Write a program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
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

# 8)Write a program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
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

# 9)Write a program to remove duplicates elements from a list.
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

# 10)Write a program to check a list is empty or not.
list = []
no = int(input("Enter length of a list "))
print("Enter elements of list ")
for i in range(no):
 l1 = int(input())
 list.insert(i,l1)
print("Enterred List is =",list)
if len(list)== 0:
 print("given list is empty")
else:
 print("given list is not empty")

# 11)Write a program to find the list of words that are longer than n from a given list of words.
def word(n, str):
 wlen = []
 text = str.split(" ")
 for x in text:
 if len(x) > n:
 wlen.append(x)
 return wlen 
print(word(3, "Hello this is python programming"))

# 12) Write a program to print the numbers of a specified list after removing even numbers from it.
list = []
no = int(input("Enter length of a list "))
print("Enter elements of list ")
for i in range(no):
 l1 = int(input())
 list.insert(i,l1)
for i in list:
 if(i%2 == 0):
 list.remove(i)
print("list after removing even numbers ")
print(list)
