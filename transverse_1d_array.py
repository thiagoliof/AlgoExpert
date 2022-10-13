from tkinter.tix import Tree
import unittest
import collections


def manipulate_arr(arr):
    low = 0
    high = len(arr) - 1
    middle = low + high // 2

    print(arr)
    
    while arr[low] <= middle and arr[high] >= middle:
        print('low: ', arr[low])
        print('high: ', arr[high])
        low = low + 1
        high = high - 1
        

if __name__ == "__main__":
    a = [0, 1, 2, 3, 4]
    manipulate_arr(a)
