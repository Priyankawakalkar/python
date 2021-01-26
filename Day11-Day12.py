# 1) Write a program to print all unique values in a dictionary.
# Program:--
dict ={}
no=int(input("Enter no of elements = "))
for i in range(no):
 key =int(input("key "))
 value =int(input("value "))
 dict[key] =value
print("dictionary is = ",dict)
print("unique values in a dictionary = ",set(dict.values())) 

# Output:--
Enter no of elements = 5
key 1
value 10
key 2
value 20
key 1
value 10
key 3
value 50
key 4
value 20
dictionary is = {1: 10, 2: 20, 3: 50, 4: 20}
unique values in a dictionary = {10, 20, 50} 

2.Write a program to create and display all combinations of letters, selecting each
letter from a different key in a dictionary.
Program:--
dict = eval(input("Enter dict "))
print("dict1 is =",dict)
list1 = dict.get('1')
list2 = dict.get('2')
for i in range(2):
 for j in range(2):
 print(list1[i]+list2[j]) 

 Output:--
Enter dict {'1':['a','b'], '2':['c','d']}
dict1 is = {'1': ['a', 'b'], '2': ['c', 'd']}
ac
ad
bc
bd 

3.Write a program to find the highest 3 values in a dictionary.
Program:--
dict ={}
no=int(input("Enter no of elements = "))
for i in range(no):
 key =int(input("key "))
 value =int(input("value "))
 dict[key] =value
print("dictionary is = ",dict)
list=sorted(set(dict.values()))
print("highest 3 values in dictionary are ",set(list[-3:])) 

Output:--
Enter no of elements = 5
key 1
value 10
key 2
value 20
key 3
value 30
key 4
value 40
key 5
value 50
dictionary is = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
highest 3 values in dictionary are {40, 50, 30} 
