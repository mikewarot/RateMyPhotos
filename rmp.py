from aesthetic_predictor import predict_aesthetic
from PIL import Image
import os

q = os.scandir('.')
for z in q:
    if z.is_file():
        if z.name.lower().endswith(('jpg', 'jpeg')):
            try:
                with Image.open(z.path) as img:
                    t = predict_aesthetic(img)
                    v = t.item()  # strip out the floating point score
                    print(z.name, v)
            except Exception as e:
                print(f"Error processing file {z.name}: {e}")
    elif z.is_dir():
        print("Found directory ", z.name)


