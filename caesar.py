ALPHABET = "abcdefghijklmnopqrstuvwxyz"
encrypted_phrase = "dspttjohuifsvcjdpoabrkttds"



if __name__ == '__main__':
    offset = 0
    for _ in range(len(ALPHABET)):
        result = ""
        for char in encrypted_phrase:
            char_index = ALPHABET.index(char)
            char_index += offset
            if char_index >= len(ALPHABET):
                char_index -= len(ALPHABET)
            result += ALPHABET[char_index]
        print(f"With offset {offset}: result is {result}")
        offset += 1
