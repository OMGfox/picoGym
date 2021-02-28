ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def create_table():
    table = list()
    current_line = ALPHABET
    for _ in range(len(ALPHABET)):
        table.append(current_line)
        current_line = (current_line + current_line[0])[1:]
    return table


def decode(phrase, key, table):
    result = ""
    for phrase_char, key_char in zip((x for x in phrase), (x for x in key)):
        key_index = ALPHABET.index(key_char)
        phrase_index = table[key_index].index(phrase_char)
        result += ALPHABET[phrase_index]
    return result


if __name__ == '__main__':
    table = create_table()
    phrase = "UFJKXQZQUNB"
    key = "SOLVECRYPTO"
    decoded_phrase = decode(phrase=phrase, key=key, table=table)
    print(f"The flag is: picoCTF{{{decoded_phrase}}}")
