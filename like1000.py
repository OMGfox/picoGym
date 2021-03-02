import tarfile

if __name__ == '__main__':
    for name in range(1000, 0, -1):
        with tarfile.open(f"/home/fiyg/Documents/CTF/picoCTF/like1000/{name}.tar") as archive:
            archive.extractall(path="/home/fiyg/Documents/CTF/picoCTF/like1000/")
            with open("/home/fiyg/Documents/CTF/picoCTF/like1000/filler.txt") as filler:
                content = filler.readlines()
                print(content)
                if "picoCTF" in content:
                    break

