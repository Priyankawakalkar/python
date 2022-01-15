#1 python program to interchange first and last elements in a  list
l1 = [12,45,89,35,78]
temp = []
for i in l1:
    temp = l1[0]
    l1[0] = l1[-1]
    l1[-1] = temp
print(l1)
