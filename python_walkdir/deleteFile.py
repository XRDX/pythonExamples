import os

for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
    for filename in filenames:
        if(filename == "A" or filename == "B" or filename == "C"):
            os.remove(os.path.join(dirpath, filename))
            print(filename + " deleted")
