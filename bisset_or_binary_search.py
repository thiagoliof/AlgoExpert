lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
i = 6

def bs(lst, i):
    
    lo = 0
    hi = len(lst)
    count = 0

    while lo < hi:
        
        print("---------------------")
        print("passada: ", count)
        print("lo: ", lo)
        print("hi: ", hi)
        print("mid", (lo + hi) // 2)
        count +=1
        
        mid = (lo + hi) // 2

        if lst[mid] < i:
            lo = mid + 1
        else:
            hi = mid
    
    return lo


if __name__ == "__main__":
    bs = bs(lst, i)
    print(bs)