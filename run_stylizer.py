import os
import argparse

myPath = 'E:/Dhruv/Projects_19-20/DeepDream/deep_dreaming_start/output'
myFiles = os.listdir(myPath)
os.system('cd ‪E:/Dhruv/Projects_19-20/DeepDream/deep_dreaming_start')
for f in myFiles:
    img_in = myPath + "/" + f
    parser = argparse.ArgumentParser(description=None)
    args = parser.parse_args()
    cmd_run = f"python neural_style.py --content {img_in} --styles content_style.jpg --output E:/Dhruv/Projects_19-20/DeepDream/deep_dreaming_start/output/final/output_{f}.jpg --iterations 250"
    os.system(cmd_run)