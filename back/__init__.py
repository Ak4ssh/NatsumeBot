import os

files = []

for filename in os.listdir("./back"):

    if filename.endswith("PNG"):

        files.append(filename[:-4])
