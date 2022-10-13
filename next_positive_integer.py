def solution(A):
    m = max(A)
    if m < 1:
       return 1

    A = set(A)
    B = set(range(1, m + 1))
    D = B - A
    if len(D) == 0:
        return m + 1
    else:
        return min(D)
            
if __name__ == "__main__":
    s = solution([1, 3, 6, 4, 1, 2, 5])
    print(s)