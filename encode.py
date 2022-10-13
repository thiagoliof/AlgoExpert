corresponding = {
    'a' :0,
    'b' :1, 
    'c' :2, 
    'd' :3, 
    'e' :4, 
    'f' :5, 
    'g' :6, 
    'h' :7, 
    'i' :8, 
    'j' :9, 
    'k' :10, 
    'l' :11, 
    'm' :12, 
    'n' :13, 
    'o' :14, 
    'p' :15, 
    'q' :16, 
    'r' :17, 
    's' :18, 
    't' :19, 
    'u' :20, 
    'v' :21, 
    'w' :22, 
    'x' :23, 
    'y' :24, 
    'z' :25
}

def convert_int_to_caracter(i):
    key_list = list(corresponding.keys())
    val_list = list(corresponding.values())
    position = val_list.index(i)
    #print(key_list[position])
    return key_list[position]

def encode(s, n):
    s_to_return = ''
    for element in s:
        value_element = corresponding[element]
        s_to_return += str(convert_int_to_caracter(value_element * n % 26))
    return str(n) + s_to_return

def decode(s):
    numbers = "".join([f"{x}" for x in s if x.isdigit()])
    str = "".join([f"{x}" for x in s if not x.isdigit()])
    
  
if __name__ == "__main__":
    #decode('1212232323qwqwqwqwqw')

    print(encode("jdgegdidjkdahjbkeelg", 761328))
    #print(encode("mer", 6015))

    
    number_key = 5057

    #print(5057 * 3 / 26)

    # for i in range(0, 10):
    #     if i % 2 == 0:
    #         print("par", i, i * number_key % 26)
    #     else:
            
    #         print("impar", i * number_key % 26)

    #print(182026 / 2)


    print("(2 * 5057)---->", 2 * 5057 % 26)
    print("(23 * 5057)---->", 23 * 5057 % 26)
    print("(19 * 5057)---->", 19 * 5057 % 26)
    print("(9 * 5057)---->", 9 * 5057 % 26)
    print("(1 * 5057)---->", 1 * 5057 % 26)
    print("(29 * 5057)---->", 29 * 5057 % 26)
    print("(30 * 5057 % 26)---->", 30 * 5057 % 26)
    print("(31 * 5057 % 26)---->", 31 * 5057 % 26)
    print("(32 * 5057 % 26)---->", 32 * 5057 % 26)
    print("---------------------------------------------")
    print("(761328 * 1 % 26)---->", 761328 * 1 % 26)
    print("(761328 * 2 % 26)---->", 761328 * 2 % 26)
    print("(761328 * 3 % 26)---->", 761328 * 3 % 26)
    print("(761328 * 4 % 26)---->", 761328 * 4 % 26)
    print("(761328 * 5 % 26)---->", 761328 * 5 % 26)
    


