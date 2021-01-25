# 1) Write a program to concatenate following dictionaries to create a new one.
# Program:--
dict1 = eval(input("Enter dict1 "))
print("dict1 is =",dict1)
dict2 = eval(input("Enter dict2 "))
print("dict2 is =",dict2)
dict3 = eval(input("Enter dict3 "))
print("dict3 is =",dict3)
dict4 ={}
for d in(dict1,dict2,dict3):
 dict4.update(d)
print("dictionary is ",dict4) 

# Output:--
Enter dict1 {'1':10}
dict1 is = {'1': 10}
Enter dict2 {'2':20}
dict2 is = {'2': 20}
Enter dict3 {'3':30}
dict3 is = {'3': 30}
dictionary is {'1': 10, '2': 20, '3': 30}

# 2) Write a Program to check whether a given key already exists in a dictionary.
# Program:--
dict = eval(input("Enter dict "))
print("dict is =",dict)
key=input("Enter key to check ")
if key in dict.keys():
 print("key is already exist in dictionary")
else:
 print("key is not exist in dictionary") 

# Output:--
Enter dict {'1':10,'2':20}
dict is = {'1': 10, '2': 20}
Enter key to check = 2
key is already exist in dictionary 

# 3) Write a Program to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Program:--
dict ={}
n = eval(input("Enter number = "))
for x in range(1,n+1):
 dict[x] = x*x
print("dict is = ",dict) 

# Output:--
Enter number = 6
dict is = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36} 

1.Write a program to remove a key from a dictionary.
Program:--
dict = eval(input("Enter dict "))
print("dict1 is =",dict)
key=input("Enter key to delete ")
if key in dict:
 del dict[key]
else:
 print("Given key is not present in dict")
print("Updated dict is ",dict) 

Output:--
Enter dict {'1':10,'2':20,'3':30,'4':40,'5':50}
dict is = {'1': 10, '2': 20, '3': 30, '4': 40, '5': 50}
Enter key to delete 3
Updated dict is {'1': 10, '2': 20, '4': 40, '5': 50}

2.Write a program to multiply all the items in a dictionary.
Program:--
dict = eval(input("Enter dict "))
print("dict is =",dict)
mul=1
for key in dict:
 mul=mul * dict[key]
print("multiplication is ",mul) 

Output:--
Enter dict {'1':5,'2':6,'3':7,'4':8}
dict is = {'1': 5, '2': 6, '3': 7, '4': 8}
multiplication is 1680 

3.Write a program to map two lists into a dictionary. 
Program:--
key = []
no1 = int(input("Enter length of a keys "))
print("Enter elements of keys ")
for i in range(no1):
 l1 = int(input())
 key.insert(i,l1)
print("key is ",key)
value = []
no2 = int(input("Enter length of a value "))
print("Enter elements of value ")
for i in range(no2):
 l2 = int(input())
 value.insert(i,l2)
print("value is ",value)
dict = dict(zip(key, value))
print("dictionary is ",dict) 

Output:--
Enter length of a keys 4
Enter elements of keys
2
3
4
5
key is [2, 3, 4, 5]
Enter length of a value 4
Enter elements of value
4
9
16
25
value is [4, 9, 16, 25]
dictionary is {2: 4, 3: 9, 4: 16, 5: 25} 
