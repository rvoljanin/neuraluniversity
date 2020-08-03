from PIL import Image, ImageChops
import numpy as np

def load_img (img,invert=0):
    size = (28,28)
    raw = Image.open(img)
    gray = raw.convert('L')
    worb = gray.point(lambda x: 0 if x<128 else 255, '1')
    resize = worb.resize(size, resample=0)

    if invert:
        resize = ImageChops.invert(resize)

    return np.array(resize)

out = load_img("gimp_data_set/nine.bmp")
#out.save("result_bw.png")
#print(out.shape)

digit = {0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
gimp = "gimp_data_set"
handwritten = "handwritten_data_set"

for i in digit:
    img_path = gimp + '/' + digit[i] + '.bmp'
    print(img_path)
