def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    #firstcColor = "RED" if redShirtHeights[0] < redShirtHeights[0] else "BLUE"

    firstcColor = ""
    if redShirtHeights[0] < redShirtHeights[0]:
        firstcColor = "RED"
    elif redShirtHeights[0] > redShirtHeights[0]:
        firstcColor = "BLUE"
    elif redShirtHeights[0] == redShirtHeights[0]:
        return False
    
    
    for i in range(len(redShirtHeights)):
        redHeight = redShirtHeights[i]
        blueHeight = blueShirtHeights[i]

        if firstcColor == 'RED':
            if redHeight >= blueHeight:
                return False
            else:
                if blueHeight >= redHeight:
                    return False
    
    return True


    # Write your code here.
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    #firstcColor = "RED" if redShirtHeights[0] < redShirtHeights[0] else "BLUE"
    
    firstcColor = ""
    if redShirtHeights[0] < blueShirtHeights[0]:
        firstcColor = "RED"
    elif redShirtHeights[0] > blueShirtHeights[0]:
        firstcColor = "BLUE"
    
    
    for i in range(len(redShirtHeights)):
        redHeight = redShirtHeights[i]
        blueHeight = blueShirtHeights[i]

        if firstcColor == 'RED':
            if redHeight >= blueHeight:
                return False
            else:
                if blueHeight >= redHeight:
                    return False
    
    return True



red_arr = [5, 8, 1, 3, 4]
blue_arr = [6, 9, 2, 4, 5]
b = classPhotos(red_arr, blue_arr)
print(b)