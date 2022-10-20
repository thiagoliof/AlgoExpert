def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort() 
    idxOne = 0
    idxTwo = 0
    smallest = float("inf")
    current = float("inf")
    par = []
    
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        first_num = arrayOne[idxOne]
        second_num = arrayTwo[idxTwo]
        if first_num == second_num:
            return [first_num, second_num]
        elif first_num > second_num:
            current = abs(first_num - second_num)
            idxTwo += 1
        elif first_num < second_num:
            current  = abs(first_num - second_num)
            idxOne += 1
    
        if smallest > current:
            smallest = current
            par = [first_num, second_num]
    
    return par
        
        


if __name__ == "__main__":
    arrayOne = [15, 3, 5, 10, 20, 28]
    arrayTwo = [15, 17, 26, 134, 135]
    sd = smallestDifference(arrayOne, arrayTwo)
    print(sd)