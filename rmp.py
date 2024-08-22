from aesthetic_predictor import predict_aesthetic
from PIL import Image
import os
q = os.scandir('.')
for z in q:
    if z.is_file():
        if z.name.endswith('JPG'):
            t = predict_aesthetic(Image.open(z.path))
            v = t.item()  # strip out the floating point score
            print(z.name, v)
    elif z.is_dir():
        print("Found directory ", z.name)


