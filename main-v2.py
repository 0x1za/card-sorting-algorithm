cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q']
sort = ['Q', 'Q', 'J', 2, 3]
sorte = []

for x in cards:
    for z in sort:
        if x == z:
            sorte.append(z)
        else:
            pass

print (sorte)