# Python program to rename all file
# names in your directory
import os

folder = 'C:/Users/12146/PycharmProjects/Platformer/imgs/enemy/Death'

# Iterate through the folder
for file in os.listdir(folder):

    for count, filename in enumerate(os.listdir(folder)):
        dst = f"{str(count)}.png"
        src = f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst = f"{folder}/{dst}"

        # rename() function will
        # rename all the files
        os.rename(src, dst)



# verify the result
res = os.listdir(folder)
print(res)