from PIL import Image
from PIL import ImageEnhance
import os


def adjust_contrast(input_image, output_image, factor):
    image = Image.open(input_image)
    enhancer_object = ImageEnhance.Contrast(image)
    out = enhancer_object.enhance(factor)
    out.save(output_image)


def adjust_brightness(input_image, output_image, factor):
    image = Image.open(input_image)
    enhancer_object = ImageEnhance.Brightness(image)
    out = enhancer_object.enhance(factor)
    out.save(output_image)


myPath = 'E:/Dhruv/Projects_19-20/DeepDream/deep_dreaming_start/output'
myFiles = os.listdir(myPath)
for f in myFiles:
    img_in = myPath + "/" + f
    img_out = f"E:/Dhruv/Projects_19-20/DeepDream/deep_dreaming_start/output/enhanced/dream_image_out{f}.jpg"
    adjust_contrast(img_in, img_out, 1.8)
    adjust_contrast(img_out, img_out, 0.8)



