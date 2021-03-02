path1 = [106, 85, 53, 116, 95, 52, 95, 98]
path2 = [0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f]
path3 = [0o142, 0o131, 0o164, 0o63 , 0o163, 0o137, 0o143, 0o61]
path4 = ['9', '4', 'f', '7', '4', '5', '8', 'e']


if __name__ == '__main__':
    result = ""
    for n in path1:
        result += chr(n)

    for n in path2:
        result += chr(n)

    for n in path3:
        result += chr(n)

    for n in path4:
        result += n

    print(result)
