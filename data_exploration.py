import os
import shutil
import pandas as pd

# to start off i'll like to take the files in this folder
# inside the folder a nice mix of jpg's and txt's files
data_path = 'raw_fooball_data/'
file_list = os.listdir(data_path)

# and separate them accordingly to each folder
data_path = 'raw_fooball_data/'
img_train_path = 'datasets/football/train/images/'
img_test_path = 'datasets/football/test/images/'
labels_train_path = 'datasets/football/train/labels/'
labels_test_path = 'datasets/football/test/labels/'

# lets start by catagorizing each by extention
labels = []
images = []
for file in file_list:
    fname, fext = file.split('.')
    if fext == 'jpg':
        images.append(file)
    elif fext == 'txt':
        labels.append(file)

if len(labels) == len(images):
    labels = sorted(labels)
    images = sorted(images)
    test_size = int(len(images)*0.2)
    train_size = len(images)-test_size

os.makedirs(img_train_path, exist_ok=True)
os.makedirs(labels_train_path, exist_ok=True)
os.makedirs(img_test_path, exist_ok=True)
os.makedirs(labels_test_path, exist_ok=True)

# populate the training directories
for item in zip(images[:train_size],labels[:train_size]):
    shutil.copy2(data_path+item[0],img_train_path)
    shutil.copy2(data_path+item[1],labels_train_path)

# populate the test directories
for item in zip(images[-test_size:],labels[-test_size:]):
    shutil.copy2(data_path+item[0],img_test_path)
    shutil.copy2(data_path+item[1],labels_test_path)
