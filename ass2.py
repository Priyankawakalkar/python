#4 Check whether each word in a string begin with upper or not. if all letter begin with upper print true otherwise false 
string = input("enter a string to check string is in title case or not : ")
if string == string.title():
    print(True)
else:
    print(False)

    
    
#5. Write python program to print all the duplicates from a given list without using set function
from collections import Counter
l1 = [1,2,2,2,3,3,4,4,5]
s1 = Counter(l1)
l2 = []
print(s1)
for key in s1:
    if s1[key] > 1:
        l2.append(key)
print(l2)



#6. print symmetric diff bet two list
l1=[1,2,8,9,6]
l2=[1,6,5,4,3]
print(set(l1).symmetric_difference(set(l2)))
