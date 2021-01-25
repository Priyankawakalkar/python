1.Write a program to concatenate following dictionaries to create a new one.
Program:--
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

Output:--
Enter dict1 {'1':10}
dict1 is = {'1': 10}
Enter dict2 {'2':20}
dict2 is = {'2': 20}
Enter dict3 {'3':30}
dict3 is = {'3': 30}
dictionary is {'1': 10, '2': 20, '3': 30}

2.Write a Program to check whether a given key already exists in a
dictionary.
Program:--
dict = eval(input("Enter dict "))
print("dict is =",dict)
key=input("Enter key to check ")
if key in dict.keys():
 print("key is already exist in dictionary")
else:
 print("key is not exist in dictionary") 

 Output:--
Enter dict {'1':10,'2':20}
dict is = {'1': 10, '2': 20}
Enter key to check = 2
key is already exist in dictionary 
