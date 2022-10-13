roman_numbers = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000,
}

def roman_to_arabian(s):
    total = 0
    i = 0
    while i < len(s):
        if i + 1 < len(s) and roman_numbers[s[i]] < roman_numbers[s[i + 1]]:
            print("passei subtract")
            total += roman_numbers[s[i + 1]] - roman_numbers[s[i]]
            i += 2
        else:
            print("passei normal")
            total+= roman_numbers[s[i]]
            i+=1

    return total

if __name__ == "__main__":
    s = "IV"
    result = roman_to_arabian(s)
    print(result)