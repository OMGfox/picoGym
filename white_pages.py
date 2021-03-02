ALPHABET = "abcdefghijklmnopqrstuvwxyz"

if __name__ == '__main__':
    with open("/home/fiyg/Documents/CTF/picoCTF/WhitePages/whitepages.txt") as doc:
        encoded_line = ""
        for char in bytearray(doc.readline(), encoding="utf-8"):
            if char == 0x20:
                encoded_line += " "
            else:
                encoded_line += "."
        encoded_chars = encoded_line.split(" ")
        decoded_line = ""
        for char in encoded_chars:
            if char == " ":
                decoded_line += "1"
            else:
                decoded_line += ("0" * (len(char) // 3)) + "1"

        result = ""
        for i in range(0, len(decoded_line), 8):
            result += chr(int(decoded_line[i:i+8], base=2))
        print(result)

