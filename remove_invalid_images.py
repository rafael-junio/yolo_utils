"""Remove all images WITHOUT a .txt file in a folder"""
import os

folder_path = f'PATH_TO_DATASET'

filename_dir = os.listdir(folder_path)

counter = 0
for filename in filename_dir:
    filename_name = os.path.splitext(f'{filename}')[0]
    filename_ext = os.path.splitext(f'{filename}')[1]
    if filename_ext == '.jpg':
        if f'{filename_name}.txt' not in filename_dir:
            counter += 1
            os.remove(os.path.join(folder_path, filename))
            print(f'{filename} excluido!')
print(f'{counter} imagens excluídas!')
