#7 write a python program to create a dictionary from a string. track count of the letters from the string.

str1 = "wakalkar"
cnt = {}
for i in str1:
    if i not in cnt:
        cnt[i] = 0
    cnt[i] += 1
print(cnt)



#8 write a python program to sort a list alphabetically in a dictionary

d1 = {'n1':[5,3,6],'n2':[4,1,8],'n3':[3,2,4],'n4':[9,8,6]}
for i in d1.values():
    i.sort()
print(d1)


#9 write a python program to combine two lists into a dictionary

l1 = ['a','b','c','d','e','f']
l2 = [ 1 , 2 , 3 , 4 , 5 ]
print(dict(zip(l1,l2)))
