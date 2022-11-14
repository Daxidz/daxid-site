import json
import os
import re


directory="content/pixelart/img/"

exts = ('.png', '.jpeg', '.jpg', '.gif')

for filename in os.listdir(directory):

    f = os.path.join(directory, filename)
    original_name=f
    original_meta_name=f+".meta"
    print(filename)
    print(original_meta_name)

    if os.path.isfile(f) and f.endswith(exts):
        meta_file = open(os.path.join(directory, filename + ".meta"))


        meta = json.load(meta_file)
        

        meta_file.close()
        dummy, ext = os.path.splitext(f)
        
        new_name = str(meta["Rating"]) + "_" + meta["Title"] + ext
        re.sub('[^a-zA-Z0-9]','', new_name)
        new_name = new_name.replace(" ", "")
        new_name = directory + new_name
        # print("Renaming " + original_name + " in " + new_name)
        os.rename(original_name, new_name)
        os.rename(original_meta_name, new_name+".meta")
        