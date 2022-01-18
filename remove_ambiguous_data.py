from PIL import Image
import os
i = 0

images = os.listdir('dataset/test')

for file in images:
    try:
        im = Image.open('dataset/test/'+file)
    except:
        i+=1
        os.remove('dataset/test/'+file)


print(i)
