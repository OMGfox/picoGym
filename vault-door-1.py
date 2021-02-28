import re

if __name__ == '__main__':
    parsed_pairs = dict()
    with open("/home/fiyg/Documents/CTF/picoCTF/vault-door-1/VaultDoor1.java") as source:
        for line in source:
            regex_pairs = re.compile(r"password.charAt\((\d{1,2})\)[ ]{1,2}== '(.)'")
            pair = regex_pairs.findall(line)[0]
            parsed_pairs[pair[0]] = pair[1]
    print(parsed_pairs)

    result = ""
    for i in range(32):
        result += parsed_pairs[str(i)]

    print(f"picoCTF{{{result}}}")
