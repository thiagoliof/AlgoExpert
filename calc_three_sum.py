from typing import List


def three_num_sum(array:List[int], target:int) -> List[int]:
    array.sort()
    triplets= []
    for i in range(len(array)):
        left = i+1
        right = len(array) - 1
        while left < right:
            current_sum = array[i] + array[left] + array[right]
            if current_sum == target:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            elif current_sum > target:
                right -=1
    return triplets
        



if __name__ == "__main__":
    arr = [12, 3, 1, 2, -6, 5, -8, 6]
    t = three_num_sum(arr, 2)
    print(t)