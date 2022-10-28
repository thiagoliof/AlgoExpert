def maxCard(cards):
    
    visited = []
    lst = []

    for i in range(0, len(cards)):
        current_cards = cards[i]
        current_cards.sort(reverse=True)

        low = 0
        high = len(current_cards)

        while low < high:
            if current_cards[low] in current_cards[low+1:high]:
                visited.append(current_cards[low])
            low += 1
    
        for card in current_cards:
            if card not in visited:
                lst.append(card)
 
    return -1 if len(lst) == 0 else max(lst)


cards = [[11, 2, 3], [3, 3, 3, 4, 4, 6, 7]]


mc = maxCard(cards)
print(mc)
