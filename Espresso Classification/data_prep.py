
import os
import shutil
import random

# Random generator seed to have consistency in chaos
random.seed(117)

# Image data directory
img_data_dir = './data'  # Adjusted this to reflect your folder structure

# Directories to distribute data
train_dir = './data/train_set'  # Paths adjusted to place inside data folder
test_dir = './data/test_set'    # Paths adjusted to place inside data folder
quiz_dir = './data/quiz_set'    # Paths adjusted to place inside data folder

categories = ['espresso', 'kenya', 'starbucks_pike_palace']


# Percentages to distribute
train_pct = 0.75  # Adjusted this according to your new split
test_pct = 0.10  # Adjusted this according to your new split
quiz_pct = 0.15  # Adjusted this according to your new split

# Ensure percentages add up to 1
assert train_pct + test_pct + quiz_pct == 1.0, 'Percentages do not add up to 1'

for category in categories:
    # Denotes img directories and creates files list
    src_dir = os.path.join(img_data_dir, 'img_dataset', category)
    files = os.listdir(src_dir)

    # Create category directories in train, test and quiz directories
    train_category_dir = os.path.join(train_dir, category)
    test_category_dir = os.path.join(test_dir, category)
    quiz_category_dir = os.path.join(quiz_dir, category)

    os.makedirs(train_category_dir, exist_ok=True)
    os.makedirs(test_category_dir, exist_ok=True)
    os.makedirs(quiz_category_dir, exist_ok=True)

    # Randomly shuffle the files
    random.shuffle(files)

    # Split files based on percentages
    train_files = files[:int(len(files)*train_pct)]
    test_files = files[int(len(files)*train_pct):int(len(files)*(train_pct + test_pct))]
    quiz_files = files[int(len(files)*(train_pct + test_pct)):]

    for file in train_files:
        shutil.move(os.path.join(src_dir, file), os.path.join(train_category_dir, file))

    for file in test_files:
        shutil.move(os.path.join(src_dir, file), os.path.join(test_category_dir, file))

    for file in quiz_files:
        shutil.move(os.path.join(src_dir, file), os.path.join(quiz_category_dir, file))