from PIL import Image
import os, sys 

#path = 'images'
path = os.path.expanduser('./images/')
new_path = os.path.expanduser('./new_images/')
#dirs = os.listdir(path)
dirs = os.listdir(path)

def resize():
    for item in dirs:
        imFile = path+item
        if (os.path.isfile(imFile) and item !='.DS_Store'):
            im = Image.open(imFile)
            f, e = os.path.splitext(new_path+item)
            imResize = im.resize((1920,1920), Image.ANTIALIAS)
            imResize.save(f + '.png','png')
resize()
