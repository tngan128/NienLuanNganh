import numpy as np
import cv2
import os
import matplotlib.pyplot as plt #thu vien doc anh va ghi anh
import random as rn
from tensorflow import keras
from keras.models import load_model

model = load_model("model_final.h5")

path = "./flowers"
IMG = []
flowers = {
    0: "Hoa Cúc",
    1: "Hoa Bồ Công Anh",
    2: "Hoa Hồng",
    3: "Hoa Hướng Dương",
    4: "Hoa Tulip"
}

fig,ax=plt.subplots(4, 4, figsize = (12, 12))
exImg = 0
Ftypes = os.listdir(path)

for i in range(4):
    for j in range(4):
        FTIdex = rn.choice(range(len(Ftypes)))
        flowerType = Ftypes[FTIdex]
        FTPath = os.path.join(path, flowerType)
        imgPath = os.path.join(FTPath, rn.choice(os.listdir(FTPath)))
        img = cv2.imread(imgPath, cv2.IMREAD_COLOR)
        img = cv2.resize(img, (150, 150))
        ax[i, j].imshow(img)
        img = np.reshape(img, [1, 150, 150, 3])

        pred = model.predict(img)
        # print(pred)
        # print(flowerType)

        ax[i, j].axis("off")
        ax[i, j].set_title(flowerType + " - " + str(flowers[np.where(pred == 1)[1][0]]), fontsize = 8)
        if FTIdex == np.where(pred == 1)[1][0]:
            exImg += 1

plt.tight_layout()
plt.suptitle(f"{exImg}/16")
plt.show()
