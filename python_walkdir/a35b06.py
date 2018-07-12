import os
import hashlib


def md5_8(url):
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()[:8]

for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
    for filename in filenames:
        md5 = md5Checksum(filename)
        new_filename = md5[:6] + os.path.splitext(filename)[1]
        print(filename, new_filename)
        os.rename(filename, new_filename)
