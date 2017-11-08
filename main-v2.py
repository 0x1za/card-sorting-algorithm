cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q']
sort = ['Q', 'Q', 'J', 2, 2, 3]
sorted = []

for x in cards:
    for i in sort:
        if x == i:
            sorted.append(i)
        else:
            pass

print (sorted)