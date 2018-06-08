import os
import hashlib

def md5Checksum(filePath):
    with open(filePath, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
    for filename in filenames:
        md5 = md5Checksum(filename)
        new_filename = md5[:6] + os.path.splitext(filename)[1]
        print(filename, new_filename)
        os.rename(filename, new_filename)
