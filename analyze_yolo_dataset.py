"""Search in the .txt yolo format files and returns how many of each class your dataset have
Mandatory: Modify folder_path and classesFile to your need"""
import os

folder_path = f'PATH_TO_DATASET'

filename_dir = os.listdir(folder_path)

classesFile = open(f'PATH_TO_CLASSES_TXT', 'r')
classes = classesFile.read().strip('\n').split('\n')

classes_counter = {}
classes_number = 0

for label in classes:
    classes_counter[f'{label}'] = 0

for filename in filename_dir:
    filename_name = os.path.splitext(f'{filename}')[0]
    filename_ext = os.path.splitext(f'{filename}')[1]
    if filename_ext == '.txt' and filename_name != 'classes':
        txt_file = open(f'{folder_path}/{filename}', 'r')
        for line in txt_file:
            classIndex, xcen, ycen, w, h = line.strip().split(' ')
            label = classes[int(classIndex)]
            if label not in classes_counter:
                classes_counter[f'{label}'] = 1
                classes_number += 1
            else:
                classes_counter[f'{label}'] += 1

sorted_classes = sorted(classes_counter.items(), key=lambda x: x[0], reverse=False)
for (label, value) in sorted_classes:
    print(f'{label}: {value}')
print(classes)
