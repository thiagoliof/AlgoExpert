from typing import List


def singleNumber(nums: List[int]) -> int:
    a = 0
    for i in nums:
        a ^= i
    return a

if __name__ == "__main__":
    sn = singleNumber([4,1,2,1,2, 4, 9])
