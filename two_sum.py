from typing import List


hashmap = {}

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [i, hashmap[diff]]
            hashmap[n] = i  


if __name__ == "__main__":
        s = Solution()
        result = s.twoSum(nums=[1, 2, 3, 4, 5, 6, 7, 8, 9], target=10)
        print(result)
