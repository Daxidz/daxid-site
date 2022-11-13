# import required module
import os
import json
from PIL import Image
from threading import Thread, Event
import psutil
# assign directory
directory = '.'
exts = ('.png', '.jpeg', '.jpg', '.gif')

METADATA_TEMPLATE = {
    "Tags": ["template_tags"],
    "Title": "template_name",
    "ColorLabels": "RGB",
    "Rating": 1
}

TAGS_LIST = {
    "p": "Portraits",
    "c": "Characters",
    "C": "Clouds",
    "l": "Landscapes",
    "a": "Anime",
    "m": "Misc",
    "b": "Bier"
}

e = Event()

def create_metadata(title, tags, file_name):
    f = open(file_name + ".meta", "a")
    metadata = METADATA_TEMPLATE.copy()
    metadata["Tags"] = tags
    metadata["Title"] = title


    with open(file_name + ".meta", "w") as outfile:
        json.dump(metadata, outfile)

def parse_tags(tags):
    final_tags = []
    for t in tags:
        print(TAGS_LIST.get(t))
        if TAGS_LIST.get(t) != None:
            print()
            final_tags.append(TAGS_LIST.get(t))

    final_tags = list(dict.fromkeys(final_tags))
    return final_tags


def close_imgviewer_windows():
    for proc in psutil.process_iter():
        if proc.name() == "Microsoft.Photos.exe":
            proc.kill()


def show_image(f, k):
    img = Image.open(f)
    img.show()
    e.wait()
    img.close()
 


for filename in os.listdir(directory):

    f = os.path.join(directory, filename)

    if os.path.isfile(f) and f.endswith(exts):
        x = Thread(target=show_image, args=(f, 0))
        x.start()
        title = input("Title: ")
        
        tags = input("Tags: ")
        tags = parse_tags(tags)
        e.set()
        close_imgviewer_windows()
        create_metadata(title, tags, f)

