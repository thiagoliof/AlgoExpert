from array import array


def isPalindrome(s):
    if list(s) == swap(list(s)):
        return True
    return False


def swap(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        arr[low], arr[high] = arr[high], arr[low] 
        low +=1
        high -=1
    
    return arr  

if __name__ == "__main__":
    s = "asdfggfdsa"
    ispalindrome = isPalindrome(s)
    print(ispalindrome)