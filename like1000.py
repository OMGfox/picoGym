import tarfile

if __name__ == '__main__':
    for name in range(1000, 0, -1):
        with tarfile.open(f"/home/fiyg/Documents/CTF/picoCTF/like1000/{name}.tar") as archive:
            
            import os
            
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(archive, path="/home/fiyg/Documents/CTF/picoCTF/like1000/")
            with open("/home/fiyg/Documents/CTF/picoCTF/like1000/filler.txt") as filler:
                content = filler.readlines()
                print(content)
                if "picoCTF" in content:
                    break

