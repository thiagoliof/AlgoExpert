def maxCard(cards):
    lst = []
    duplicate = []
    maxCard = float("-inf")
    for i in range(0, len(cards)):
        _cards = cards[i]
        _cards.sort(reverse=True)
        if len(_cards) == 1 and _cards[0] > maxCard:
            lst.append(_cards[0])
            maxCard = _cards[0]
        for j in range(1, len(_cards)):
            card = _cards[j]
            previews_card = _cards[j-1]
            
            if card == previews_card:
                duplicate.append(card)
            
            if previews_card > maxCard and previews_card not in duplicate:
                lst.append(previews_card)
                maxCard = previews_card
           

    return -1 if len(lst) == 0 else max(lst)
        
cards = [
    [5, 7, 3, 9, 4, 9, 8, 3, 1], 
    [1, 2, 2, 4, 4, 1], 
    [1, 2, 3]
]

cards = [[5, 3, 6, 6, 6], [9, 9]]

mc = maxCard(cards)
print(mc)
