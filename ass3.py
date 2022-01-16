#7 write a python program to create a dictionary from a string. track count of the letters from the string.

str1 = "wakalkar"
cnt = {}
for i in str1:
    if i not in cnt:
        cnt[i] = 0
    cnt[i] += 1
print(cnt)
