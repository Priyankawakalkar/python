#1 python program to interchange first and last elements in a  list
l1 = [12,45,89,35,78]
temp = []
for i in l1:
    temp = l1[0]
    l1[0] = l1[-1]
    l1[-1] = temp
print(l1)

#2 find sum and average of list in python
l1 = [12,10,32,22]
for i in l1:
    sum1 = sum(l1)
    avg = sum1 // len(l1)
print(f"Sum of list is: {sum1} \nAverage of list is: {avg}")

#3 python program to find second largest number in a list
l1 = [23,45,89,32,65]
l1.sort()
print(f"Second largest number in sorted list is: {l1[-2]}")
