list_ish = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

list_new = [list_ish[i] for i in range (1, len(list_ish)) if list_ish[i] > list_ish[i -1]]

print(list_new)