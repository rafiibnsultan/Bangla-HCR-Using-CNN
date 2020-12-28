from __future__ import print_function
from keras.layers import Input, Dense, Convolution2D, MaxPooling2D, UpSampling2D
from keras.models import Model
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(1337)  # for reproducibility
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from PIL import Image
from os import listdir
import cv2
import numpy as np
from keras.callbacks import TensorBoard
import gzip
import cPickle
# def invertBackground():

    # for i in range(172,221):
    #     for filename in listdir("dataset/Train/" + str(i)):
    #         if filename.endswith(".bmp"):
    #             FILE = "dataset/Train/" + str(i) + "/" + filename
    #             print(FILE)
    #             image = Image.open(FILE)
    #             if (image.mode != 'P'):
    #                 inverted_image = PIL.ImageOps.invert(image)
    #                 if filename.endswith('.bmp'):
    #                     filename = filename[:-4]
    #                 FILE2 = "dataset/Train/" + str(i) + "/" + filename + ".bmp"
    #                 inverted_image.save(FILE2)
    #                 # print(FILE2)
    #         else:
    #             continue

    # for i in range(172,221):
    #     for filename in listdir("dataset/Test/" + str(i)):
    #         if filename.endswith(".bmp"):
    #             FILE = "dataset/Test/" + str(i) + "/" + filename
    #             print(FILE)
    #             image = Image.open(FILE)
    #             if (image.mode != 'P'):
    #                 inverted_image = PIL.ImageOps.invert(image)
    #                 if filename.endswith('.bmp'):
    #                     filename = filename[:-4]
    #                 FILE2 = "dataset/Test/" + str(i) + "/" + filename + ".bmp"
    #                 inverted_image.save(FILE2)
    #                 # print(FILE2)
    #         else:
    #             continue


def resizeImage():
    for i in range(172, 222):
        for filename in listdir("dataset/Train/" + str(i)):
            if filename.endswith(".bmp"):
                print(filename)

                img=cv2.imread("dataset/Train/"+str(i)+"/"+filename)
                image = np.asarray(img)
                print(image.shape)
                img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
                image=np.asarray(img)
                print(image.shape)
                img=cv2.resize(img,(28,28))
                cv2.imwrite("dataset/Train/"+str(i)+"/"+filename,img)

    for i in range(172, 222):
        for filename in listdir("dataset/Test/" + str(i)):
            if filename.endswith(".bmp"):
                print(filename)

                img = cv2.imread("dataset/Test/" + str(i) + "/" + filename)
                image = np.asarray(img)
                print(image.shape)
                img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
                image = np.asarray(img)
                print(image.shape)
                img = cv2.resize(img, (28, 28))
                cv2.imwrite("dataset/Test/" + str(i) + "/" + filename, img)

def PreParePickle():
    X_train = []
    y_train = []

    X_test = []
    y_test = []
    for i in range(172, 222):
        for filename in listdir("dataset/Train/" + str(i)):
            if filename.endswith(".bmp"):
                img = cv2.imread("dataset/Train/" + str(i) + "/" + filename)
                img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
                image = np.asarray(img)
                X_train.append(image)
                y_train.append(i%172)
            else:
                continue
        print(len(X_train))
    for i in range(172, 222):
        for filename in listdir("dataset/Test/" + str(i)):
            if filename.endswith(".bmp"):
                img = cv2.imread("dataset/Test/" + str(i) + "/" + filename)
                img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
                image = np.asarray(img)
                X_test.append(image)
                y_test.append(i%172)
            else:
                continue
    print(len(y_train))
    total_data=(X_train,y_train),(X_test,y_test)
    f = gzip.open('Nahidspickle' + '.pkl.gz', 'wb')
    cPickle.dump(total_data, f, protocol=2)
    f.close()

PreParePickle()