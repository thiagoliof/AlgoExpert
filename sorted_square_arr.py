def sortedSquaredArray(array):
    # Write your code here.
    n = len(array)
    result = [0] * n
    left = 0
    right = n - 1

    for i in range(n - 1, -1, -1):
        
        # print('index:', i)
        # print('array[left]:', abs(array[left]))
        # print('array[right]:', abs(array[right]))
        # print(array)
        

        if abs(array[left]) < abs(array[right]):
            square = array[right] * array[right]
            right -= 1
        else:
            square = array[left] * array[left]
            left += 1
        
        result[i] = square
        # print("result", result)
        # print("----------------")
    
    return result

            


if __name__ == "__main__":
    array = [-5, -4, -3, -2, -1, 4, 5, 9 ,10]
    a = sortedSquaredArray(array)
    print(array)






