character = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
code = ['01', '1000', '1010', '100', '0', '0010', '110', '0000', '00', '0111', '101', '0100', '11', '10', '111', '0110',
        '1101', '010', '000', '1', '001', '0001', '011', '1001', '1011', '1100', '11111', '01111', '00111', '00011',
        '00001', '00000', '10000', '11000', '11100', '11110']

table_to_decode = dict(zip(code, character))


encoded_message = ".--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. " \
                  "...-- ----. ----- ..--- ----- .---- ----. ..... .---- ----. } "


def preparation_to_decode(encoded_char):
    decoded_char = encoded_char.replace(".", "0").replace("-", "1")
    return decoded_char


if __name__ == '__main__':
    result = ""
    for char in encoded_message.split():
        if char in "{}":
            result += char
        else:
            key = preparation_to_decode(char)
            result += table_to_decode[key]
    print(result)
