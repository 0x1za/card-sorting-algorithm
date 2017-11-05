cards = [9, 10, 'J', 'K', 'Q', 4, 5, 6, 7, 8,'A', 2, 3]
#######################################################
# Convert cars to their numerical equivalent          #
# Example:[9, 10, 11, 12, 13, 4, 5, 6, 7, 8, 1, 2, 3] #
#######################################################
converted_cards = []
for i in cards:
    if i == 'A':
        converted_cards.append(1)
    elif i == 'J':
        converted_cards.append(11)
    elif i == 'K':
        converted_cards.append(12)
    elif i == 'Q':
        converted_cards.append(13)
    else:
        converted_cards.append(i)

sort = []
z = 0 
while z < len(cards): 
    smallest = converted_cards[0]
    for x in converted_cards:
        if x < smallest:
            smallest = x
        else:
            pass
    converted_cards.remove(smallest)
    #print (converted_cards)
    sort.append(smallest)
    #print (sort)
    z+=1
print (sort)
#######################################################
# Convert numerical values to their card equivalent   #
# Example: [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, K, Q]   #
#######################################################
    
        