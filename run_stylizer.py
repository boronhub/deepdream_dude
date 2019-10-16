import os
import argparse

myPath = 'your-path-here'
myFiles = os.listdir(myPath)
os.system('your-path-here')
for f in myFiles:
    img_in = myPath + "/" + f
    parser = argparse.ArgumentParser(description=None)
    args = parser.parse_args()
    cmd_run = f"python neural_style.py --content {img_in} --styles content_style.jpg --output your-path-here/output/final/output_{f}.jpg --iterations 250"
    os.system(cmd_run)
