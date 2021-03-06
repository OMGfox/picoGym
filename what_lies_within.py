from PIL import Image


if __name__ == '__main__':
    im = Image.open("/home/fiyg/Documents/CTF/picoCTF/What_Lies_Within/buildings.png")
    pix = im.load()
    width, height = im.size
    bin_str = ""
    try:
        for i in range(width):
            for j in range(height):
                bin_str += bin(pix[j, i][0])[-1] + bin(pix[j, i][1])[-1] + bin(pix[j, i][2])[-1]
    except:
        pass


    result = ""
    block_size = len(bin_str)
    for i in range(0, block_size, 8):
        block = bin_str[i: i + 8]
        result += chr(int(block, base=2))
    print(result)
