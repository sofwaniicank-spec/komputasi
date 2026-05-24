import cv2
import numpy as np
import os
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import euclidean_distances


dataset_path = "dataset"

faces = []
labels = []

IMG_SIZE = (100, 100)

for person_name in os.listdir(dataset_path):

    person_folder = os.path.join(dataset_path, person_name)

    for image_name in os.listdir(person_folder):

        image_path = os.path.join(person_folder, image_name)

        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        img = cv2.resize(img, IMG_SIZE)

        img_vector = img.flatten()

        faces.append(img_vector)
        labels.append(person_name)

faces = np.array(faces)

mean_face = np.mean(faces, axis=0)

A = faces - mean_face

svd = TruncatedSVD(n_components=20)

eigenfaces = svd.fit_transform(A)

test_image_path = r"D:\Project KAL\dataset\bayu\coba.png"

test_img = cv2.imread(test_image_path, cv2.IMREAD_GRAYSCALE)

if test_img is None:
    print("Gambar test tidak ditemukan!")
    exit()

test_img = cv2.resize(test_img, IMG_SIZE)

test_img = cv2.imread(test_image_path, cv2.IMREAD_GRAYSCALE)

test_img = cv2.resize(test_img, IMG_SIZE)

test_vector = test_img.flatten()

test_vector = test_vector - mean_face

test_projection = svd.transform([test_vector])

distances = euclidean_distances(test_projection, eigenfaces)

best_match_index = np.argmin(distances)

hasil = labels[best_match_index]

print("Wajah paling mirip adalah :", hasil)