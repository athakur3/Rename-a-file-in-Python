import os

path = "/Users/Username/Path_to_your_file.py"
newPath = "/Users/Username/New_Path_to_your_file.py"

def rename():
       os.rename(path, os.path.join(path + newPath))

rename()



# To execute this file, open terminal and enter 'python3 filename.py'
