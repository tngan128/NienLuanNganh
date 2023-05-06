from flask import Blueprint, render_template, redirect, url_for, request, flash, send_from_directory, current_app, jsonify
from werkzeug.utils import secure_filename
import os
from flowerR.FRModel.services import (getflowerID)
import traceback

FGModel = Blueprint("FGModel", __name__)
UPLOADFOLER = os.path.dirname(__file__)

# @FGModel.route("/recognize", methods = ['GET', 'POST'])
# def uploadImage():
#     # try:
#     #     if request.method == 'POST':
#     #         image = request.files['img']
#     #         if image.filename == "":
#     #             return redirect(request.url)
#     #         if image:
#     #             imgName = secure_filename(image.filename)
#     #             fileName = "image" + os.path.splitext(imgName)[1]
#     #             image.save(os.path.join(current_app.config['UPLOAD_FOLDER'], fileName))
#     #             result = predictAImage(os.path.join(current_app.config['UPLOAD_FOLDER'], fileName))
#     #             return render_template("recognize.html", fileURL = "..\\static\\uploads\\" + fileName, flowerName = result)
#     # except: traceback.print_exc()
#     return render_template("recognize.html")

# @FGModel.route("/image/getImageURL/<fileName>")
# def getImageURL(fileName):
#     return os.path.join(current_app.config['UPLOAD_FOLDER'], fileName)

@FGModel.route("/getResult", methods = ['POST'])
def getResult():
    return getflowerID()