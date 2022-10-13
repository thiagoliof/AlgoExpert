def minimumWaitingTime(queries):
    # Write your code here.
    #queries.sort()
    total = 0
    for idx, value in enumerate(queries):
        
        if idx == 0:
            total = 0
        else:
            for i in range(idx):
                total = total + queries[i]

        
        # if idx == 1:
        #     total = total + queries[0]
        # if idx == 2:
        #     total = total + queries[0] + queries[1] 
        # if idx == 3:
        #     total = total + queries[0] + queries[1] + queries[2] 
        # if idx == 4:
        #     total = total + queries[0] + queries[1] + queries[2] + queries[3]


    return total
    
def minimumWaitingTime2(queries):
    # Write your code here.
    
    queries.sort()
    print(queries)
    waitingTime = 0

    for idx, duration in enumerate(queries):
        left = len(queries) - (idx + 1)
        waitingTime += duration * left

        print("--------------------")
        print('left', left)
        print('duration', duration)
        print('waitingTime', waitingTime)
        print("--------------------")

        a = 'a'

    return waitingTime

if __name__ == "__main__":
    a = [6, 1, 2, 2, 3]
    b = minimumWaitingTime2(a)
    #print(b)



