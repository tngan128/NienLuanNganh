from flask import request, current_app, jsonify
from tensorflow import keras
from keras.models import load_model
import cv2
import numpy as np
import os

flowers = ['Cúc', 'Bồ công Anh', 'Hồng', 'Hướng Dương', 'Tulip']
# model = load_model(os.path.dirname(__file__) + r"\model.h5")



# def predictAImage(imgPath):
#     try:
#         img = cv2.imread(imgPath, cv2.IMREAD_COLOR)
#         img = cv2.resize(img, (150, 150))
#         img = np.reshape(img, [1, 150, 150, 3])

#         pred = model.predict(img)
#         # print({flowers[x] : pred[0][x] for x in range(len(flowers))})
#         return flowers[np.where(pred == 1)[1][0]]
#         # return {flowers[x] : int(pred[0][x]) for x in range(len(flowers))}
#     except:
#         return "Error"


def getflowerID():
    model = load_model(current_app.config['DLMODEL'])

    # read image file string data
    filestr = request.files['file'].read()
    # convert string data to numpy array
    npimg = np.fromstring(filestr, np.uint8)
    # convert numpy array to image
    img = cv2.imdecode(npimg, cv2.IMREAD_UNCHANGED)


    img = cv2.resize(img, (150, 150))
    img = np.reshape(img, [1, 150, 150, 3])

    pred = model.predict(img)
    
    return jsonify({'flowerID': int(np.where(pred == 1)[1][0])})
