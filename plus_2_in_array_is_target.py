def twoNumberSum(array, targetSum):

    array.sort()
    left = 0
    right = len(array) - 1

    count = 0

    while left < right: 
        currentSum = array[left] + array[right]
        print('passei', count)
        print('array[left]:', array[left])
        print('array[right]:', array[right])
        print('currentSum:', currentSum)
        print('target', targetSum)
        
        print('*******************************')

        if currentSum == targetSum:
            return[array[left], array[right]]
        elif currentSum < targetSum: 
            left += 1
        elif currentSum > targetSum: 
            right -= 1

        count += 1

    return []

if __name__ == "__main__":
    array = [-4, -1, 1, 3, 5, 6, 8, 11]
    targetSum = 5
    tns = twoNumberSum(array, targetSum)
    print(tns)


