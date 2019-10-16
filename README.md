# deepdream_dude
project files of deepdream video generator, similar to effect seen at https://www.youtube.com/watch?v=5WqFqzeLpXg


requirements:
tensorflow
random
matplotlib
numpy
scipy

steps:

1. run dream_image on a random group of images according to the style you want to be overlayed.
2. choose an image and use it as content_style.jpg and run  run_stylizer.py for the images
3. use after effects, or a python script to join stylized images into video

NOTE: each image takes 120 seconds to render on a GTX 1080.
