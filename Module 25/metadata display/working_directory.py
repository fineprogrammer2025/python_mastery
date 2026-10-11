import os
dirpath = os.getcwd()
print("your current working director is: ", dirpath)
print("-------------------------------------------")
foldername = os.path.basename(dirpath)
print("The directory name is: ", foldername)