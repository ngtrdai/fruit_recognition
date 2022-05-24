import os
import numpy as np
import cv2 as cv
from os import listdir
import pickle
from sklearn.preprocessing import LabelBinarizer

def saveData(rawFolder):
    kichThuocAnh = (256, 256)
    print("Bắt đầu xử lí...")
    images = []
    labels = []

    for folder in listdir(rawFolder):
        print("Folder=",folder)
        for file in listdir(rawFolder  + folder):
            print("File=", file)
            img = cv.imread(rawFolder  + folder +"/" + file)
            images.append(cv.resize(cv.cvtColor(img, cv.COLOR_BGR2RGB),dsize=(256,256)))
            labels.append(folder)
    images = np.array(images)
    labels = np.array(labels) #.reshape(-1,1)
    encoder = LabelBinarizer()
    labels = encoder.fit_transform(labels)
    print(labels)

    file = open('./dataset/fruit.data', 'wb')
    pickle.dump((images,labels), file)
    file.close()
    return 


def main():
    saveData("./dataset/")


if __name__ == "__main__":
    main()