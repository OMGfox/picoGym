ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def rot13_decode(phrase):
    result = ""
    for char in phrase:
        if char in "{}_":
            result += char
            continue
        char_index = ALPHABET.index(char)
        result += ALPHABET[char_index - 13]
    return result


if __name__ == "__main__":
    phrase = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"
    print(rot13_decode(phrase).lower().replace("ctf", "CTF"))
