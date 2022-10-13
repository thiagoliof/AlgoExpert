def isValidSubsequence(array, sequence):
    
    arrMainIDx = 0
    arrSequenceIDx = 0
    # Write your code here.

    while arrMainIDx < len(array) and arrSequenceIDx < len(sequence):
        if array[arrMainIDx] == sequence[arrSequenceIDx]:
            arrSequenceIDx += 1
        
        arrMainIDx += 1

    return arrSequenceIDx == len(sequence)
    

if __name__ == "__main__":
    array = [5, 1, 22, 25, 6, -1, 8, 10, 7]
    sequence = [1, 6, 10]
    print(isValidSubsequence(array, sequence))

1
1