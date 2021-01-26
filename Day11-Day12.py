1.Write a program to print all unique values in a dictionary.
Program:--
dict ={}
no=int(input("Enter no of elements = "))
for i in range(no):
 key =int(input("key "))
 value =int(input("value "))
 dict[key] =value
print("dictionary is = ",dict)
print("unique values in a dictionary = ",set(dict.values())) 

Output:--
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
