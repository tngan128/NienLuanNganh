import os

import numpy as np
from sklearn.model_selection import KFold
import tqdm
import cv2
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Conv2D, Dense, MaxPooling2D, Flatten, Activation
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator

import matplotlib.pyplot as plt #thu vien doc anh va ghi anh
import random as rn


dataPath = "./flowers"

daisysPath = "./flowers/daisy"
dandelionsPath = "./flowers/dandelion"
rosesPath = "./flowers/rose"
sunflowersPath = "./flowers/sunflower"
tulipsPath = "./flowers/tulip"

imgSize = 150

X = []
Y = []
lables = []

def loadData(path, flowerType):
    for img in os.listdir(path):
        imgsPath = os.path.join(path, img)
        img = cv2.imread(imgsPath, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (imgSize, imgSize))

        X.append(img)
        lables.append(str(flowerType))

def buildModel(inputShape = (150, 150, 3)):
    model = Sequential()
    model.add(Conv2D(filters = 32, kernel_size = (5,5),padding = 'Same',activation ='relu', input_shape = (150,150,3)))
    model.add(MaxPooling2D(pool_size=(2,2)))


    model.add(Conv2D(filters = 64, kernel_size = (3,3),padding = 'Same',activation ='relu'))
    model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))
    

    model.add(Conv2D(filters =96, kernel_size = (3,3),padding = 'Same',activation ='relu'))
    model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))

    model.add(Conv2D(filters = 96, kernel_size = (3,3),padding = 'Same',activation ='relu'))
    model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2)))

    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dense(5, activation = "softmax"))

    model.compile(optimizer=Adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])
    model.summary()
    return model

def main():
    global X, lables, Y
    loadData(daisysPath, "Daisy")
    loadData(dandelionsPath, "Dandelion")
    loadData(rosesPath, "Rose")
    loadData(sunflowersPath, "Sunflower")
    loadData(tulipsPath, "Tulip")

    X = np.array(X)
    le=LabelEncoder()
    Y=le.fit_transform(lables)
    Y=to_categorical(Y,5)

    model = buildModel()

    # Số lượng fold
    num_folds = 10
    epochNum = 10
    batchSize = 64

    # Chia dữ liệu ra thành từng fold
    kfold = KFold(n_splits=num_folds, shuffle=True)

    # Khởi tạo danh sách để lưu kết quả
    results = []

    # Lặp qua các fold và huấn luyện mô hình
    for fold, (train_indices, val_indices) in enumerate(kfold.split(X, Y)):
        print(f"Fold {fold+1}")
        x_train, y_train = X[train_indices], Y[train_indices]
        x_val, y_val = X[val_indices], Y[val_indices]


        # Tạo data generator cho training data
        train_datagen = ImageDataGenerator(
            rescale=1./255,
            rotation_range=10, 
            zoom_range = 0.1,
            width_shift_range=0.2,
            height_shift_range=0.2,
            horizontal_flip=True,
            vertical_flip=False)

        # Tạo data generator cho validation data
        val_datagen = ImageDataGenerator(rescale=1./255)


        # Fit model trên data generator
        model.fit(
            train_datagen.flow(x_train, y_train, batch_size=batchSize),
            steps_per_epoch=len(x_train) // batchSize,
            epochs=epochNum,
            validation_data=val_datagen.flow(x_val, y_val),
            validation_steps=len(x_val) // batchSize
        )

        # Đánh giá model và lưu kết quả vào danh sách
        scores = model.evaluate(val_datagen.flow(x_val, y_val), verbose=0)
        print(f"Accuracy: {scores[1]*100:.2f}%\n")
        results.append(scores[1] * 100)
    
    # Tính toán và in ra kết quả trung bình và độ lệch chuẩn
    print(f"Mean Accuracy: {np.mean(results):.2f}%")
    print(f"Standard Deviation: {np.std(results):.2f}")

    model.save("model_final.h5")
    


if __name__ == "__main__":
    main()