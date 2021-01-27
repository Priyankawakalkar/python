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

# 2) Write a program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
# Program:--
dict = eval(input("Enter dict "))
print("dict1 is =",dict)
list1 = dict.get('1')
list2 = dict.get('2')
for i in range(2):
 for j in range(2):
 print(list1[i]+list2[j]) 
 Program:--
str=input("Enter a string ")
print("String is ",str)
count={}
for x in str:
 if x in count.keys():
 count[x]+=1
 else:
 count[x]=1
print("count of the letters is ",count)

# Output:--
Enter dict {'1':['a','b'], '2':['c','d']}
dict1 is = {'1': ['a', 'b'], '2': ['c', 'd']}
ac
ad
bc
bd 

# 3) Write a program to find the highest 3 values in a dictionary.
# Program:--
dict ={}
no=int(input("Enter no of elements = "))
for i in range(no):
 key =int(input("key "))
 value =int(input("value "))
 dict[key] =value
print("dictionary is = ",dict)
list=sorted(set(dict.values()))
print("highest 3 values in dictionary are ",set(list[-3:])) 

# Output:--
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

# 4) Write a Python program to combine values in python list of dictionaries. Go to the editor 
# Program:--
d1=eval(input("Enter dict1 "))
d2=eval(input("Enter dict2 "))
d3=eval(input("Enter dict3 "))
l1=[d1,d2,d3]
print("list of dictionaries is",l1)
list=[]
for d in l1:
 list.append(tuple(d.values()))
dict={}
for i in list:
 if i[0] in dict:
 dict[i[0]]+=i[1]
 else:
 dict[i[0]]=i[1]
print("new dictionary is ",dict) 

# Output:--
Enter dict1 {'item': 'item1', 'amount': 400}
Enter dict2 {'item': 'item2', 'amount': 300}
Enter dict3 {'item': 'item1', 'amount': 750}
list of dictionaries is [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300},
{'item': 'item1', 'amount': 750}]
new dictionary is {'item1': 1150, 'item2': 300}

# 5) Write a Python program to create a dictionary from a string. Go to the editor
# Program:--
str=input("Enter a string ")
print("String is ",str)
count={}
for x in str:
 if x in count.keys():
 count[x]+=1
 else:
 count[x]=1
print("count of the letters is ",count) 

# Output:--
Enter a string wakalkar
String is wakalkar
count of the letters is {'w': 1, 'a': 3, 'k': 2, 'l': 1, 'r': 1}

# 6) Write a Python program to get the top three items in a shop. Go to the editor
# Program:-- 
dict={}
n=int(input("Enter elements "))
for i in range(n):
 key = (input("key "))
 value=float(input("value "))
 dict[key]=value
print("dictionary is ",dict)
a=sorted(dict.items(),key=lambda x:x[1],reverse=True)
print("top three items = ")
for i in a[:3]:
 print(i) 

 Output:--
Enter elements 5
key 1 
value 45.50
key 2
value 34
key 3
value 41.30
key 4
value 55
key 5
value 12.0
dictionary is {'1': 45.5, '2': 34.0, '3': 41.3, '4': 55.0, '5': 12.0}
top three items =
('4', 55.0)
('1', 45.5)
('3', 41.3)
