def reverseWordsInString(string):
    
    characters = [char for char in string]
    reverse_list(characters, 0, len(characters) - 1)

    # ['!', 'i', 'u', 'q', 'a', ' ', 'u', 'o', 't', 's', 'e', ' ', 'u', 'e', ' ', ',', 'a', 't', 'u', 'a', 'n', 'o', 'r', 't', 's', 'a', ' ', 'o', 'l', 'a']
    # len 30
    
    start_of_word = 0

    while start_of_word < len(characters):
        end_of_word = start_of_word

        while end_of_word < len(characters) and characters[end_of_word] != " ":
            end_of_word += 1

        reverse_list(characters, start_of_word, end_of_word - 1)
        start_of_word = end_of_word + 1

    return "".join(characters)


def reverse_list(list, start, end):
    while start < end:
        list[start], list[end] = list[end], list[start]
        start+=1
        end-=1

if __name__ == "__main__":
    print(reverseWordsInString("alo astronauta, eu estou aqui!"))
