import nibabel as nib
import numpy as np
import os

def load_mri_image(file_path):
    img = nib.load(file_path)
    data = img.get_fdata()
    return data

def normalize_and_flatten(data):
    if np.max(data) > 0:
        data = data / np.max(data)
    return data.flatten()

def load_dataset(mri_dir, labels_dict):
    X = []
    y = []
    for fname in os.listdir(mri_dir):
        if fname.endswith(".nii") or fname.endswith(".nii.gz"):
            full_path = os.path.join(mri_dir, fname)
            img_data = load_mri_image(full_path)
            X.append(normalize_and_flatten(img_data))
            y.append(labels_dict.get(fname, 0))  # default label is 0 (control)
    return np.array(X), np.array(y)
