lst = [55, 7, 78, 12, 42]

for i in range(len(lst)-1, 0, -1) :
    for j in range(i) :
        if lst[j] > lst[j+1] :
            tmp = lst[j]
            lst [j] = lst[j+1]
            lst[j+1] = tmp

print(lst)
# [7, 12, 42, 55, 78]
