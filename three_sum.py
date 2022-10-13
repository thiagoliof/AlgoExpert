from logging.handlers import SocketHandler
from turtle import right
from typing import List



class Solution:
    def threeSum(self, arr: List[int], target: int) -> List[int]:
        arr.sort()
        triplets = []
        for i in range(len(arr)):
            left = i + 1
            right = len(arr) - 1
            current_item = arr[i]
            while left < right:
                current_left = arr[left]
                current_right = arr[right]
                candidateSum = arr[i] + arr[left] + arr[right]
                if candidateSum == target:
                    triplets.append([arr[i], arr[left], arr[right]])
                    left += 1
                    right -= 1
                elif candidateSum < target:
                    left += 1
                elif candidateSum > target:
                    right -= 1
        
        return triplets


if __name__ == "__main__":
    arr = [12, 3, 1, 2, -6, 5, -8, 6]
    target = 0
    solution = Solution()
    triplets = solution.threeSum(arr, target)
    print(triplets)

