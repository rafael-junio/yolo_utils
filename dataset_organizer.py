"""This program read all of your files and rename them according to the first label in the .txt file
Example:
    Before:
        12.txt
        12.jpg
        4543-dsa.txt
        4543-dsa.txt
    After
        cat-1.txt
        cat-1.jpg
        dog-2.txt
        dog-2.txt"""
import os

folder_path = f'PATH_TO_DATASET'

filename_dir = os.listdir(folder_path)

classesFile = open(f'PATH_TO_CLASSES_TXT', 'r')
classes = classesFile.read().strip('\n').split('\n')

counter = 0

for filename in filename_dir:
    filename_name = os.path.splitext(f'{filename}')[0]
    filename_ext = os.path.splitext(f'{filename}')[1]
    if filename_ext == '.txt' and filename_name != 'classes':
        txt_file = open(f'{folder_path}/{filename}', 'r')
        for line in txt_file:
            classIndex, xcen, ycen, w, h = line.strip().split(' ')
            label = classes[int(classIndex)]
            os.rename(f'{folder_path}/{filename_name}.txt', f'{folder_path}/{label}-{counter}.txt')
            os.rename(f'{folder_path}/{filename_name}.jpg', f'{folder_path}/{label}-{counter}.jpg')
            counter += 1
            break
