'''
layer 1: wavy
layer 2: lines
layer 3: boxes
layer 4: circles
layer 6: dogs, bears, cute animals
layer 7: faces, buildings
layer 8: fish begin to appear, trippyEyes
layer 10: bandars, chipkalis, saanps
'''

from deepdreamer import model, load_image, recursive_optimize
import numpy as np
import PIL.Image
import os

layer_tensor = model.layer_tensors[1]
myPath = 'enter-path-here'
myFiles = os.listdir(myPath)
for f in myFiles:
    file_name = myPath + "/" + f
    print(file_name)
    img_result = load_image(filename='{}'.format(file_name))
    img_result = recursive_optimize(layer_tensor=layer_tensor, image=img_result,
                                    num_iterations=20, step_size=1.0, rescale_factor=0.5,
                                    num_repeats=8, blend=1.6)
    img_result = np.clip(img_result, 0.0, 255.0)
    img_result = img_result.astype(np.uint8)
    result = PIL.Image.fromarray(img_result, mode='RGB')
    result.save(f'enter-path-here/dream_image_out_{f}')
    result.show()







