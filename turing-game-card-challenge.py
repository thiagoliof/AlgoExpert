def maxCard(cards):
    maxCard = float("-inf")
    for i in range(0, len(cards)):
        
        current_cards = cards[i]
        current_cards.sort(reverse=True)

        low = 0
        high = len(current_cards)
        visited = []
        
        while low < high:
            if current_cards[low] in current_cards[low+1:high]:
                visited.append(current_cards[low])
            low += 1
    
        for card in current_cards:
            if card not in visited:
                if maxCard < card:
                    maxCard = card
 
    return -1 if maxCard == float("-inf") else maxCard


cards = [[11, 11], [1, 1, 54]]


mc = maxCard(cards)
print(mc)
