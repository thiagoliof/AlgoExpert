var_blocks = {
  "blocks": [
    {
      "gym": False,
      "school": True,
      "store": False
    },
    {
      "gym": True,
      "school": False,
      "store": False
    },
    {
      "gym": True,
      "school": True,
      "store": False
    },
    {
      "gym": False,
      "school": True,
      "store": False
    },
    {
      "gym": False,
      "school": True,
      "store": True
    }
  ],
  "reqs": ["gym", "school", "store"]
}

def apartmentHunting(blocks, reqs):
    maxDistance = [float("-inf") for _ in blocks]
    for i in range(len(blocks)):
        print("for de fora:", i)
        print("----------------------")
        for req in reqs:
            print("\tfor de reqs:", req)
            closestReqDistance = float("inf")
            for j in range(len(blocks)):
                print("\t\tfor de dentro:", j)
                if blocks[j][req]:
                    closestReqDistance = min(closestReqDistance, distanceBetween(i, j))
            print("\talimentando o array")
            print("\t-------------------")
            maxDistance[i] = max(maxDistance[i], closestReqDistance)

    return getIdxMinValue(maxDistance)

def distanceBetween(i, j):
    return abs(i - j)

def getIdxMinValue(array):
    idxAtMinvalue = 0
    minValue = float("inf")

    for i in range(len(array)):
        current_value = array[i]
        if current_value < minValue:
            minValue = current_value
            idxAtMinvalue = i
    return idxAtMinvalue 


if __name__ == "__main__":
    blocks = var_blocks["blocks"]
    reqs = var_blocks["reqs"]
    ah = apartmentHunting(blocks=blocks, reqs=reqs)
    print(ah)
     
    
    
                
            
          



                
