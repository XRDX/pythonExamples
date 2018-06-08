import os

for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
    for filename in filenames:
        print(filename)
        print(os.path.join(dirpath, filename))
