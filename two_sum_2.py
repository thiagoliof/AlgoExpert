def twoNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    lo = 1
    hi = len(array)

    for i in range(len(array)):
        while lo < hi:
            if array[i] + array[lo] == targetSum:
                return [array[i], array[lo]]
            lo += 1
                



if __name__ == "__main__":
        result = twoNumberSum(array=[1, 2, 3, 4, 5, 6, 7, 8, 9], targetSum=10)
        print(result)
