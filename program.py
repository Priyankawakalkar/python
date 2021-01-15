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
