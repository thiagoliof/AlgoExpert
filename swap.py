
from typing import List


def swap_array(arr:List) -> List:

    low = 0
    high = len(arr) - 1

    while low < high:
        arr[low], arr[high] = arr[high], arr[low]
        print("-------------------")
        print(arr)
        print("-------------------")
        low += 1
        high -=1 




if __name__ == "__main__":
    arr = [i for i in range(0, 30)]
    swap_array(arr)


