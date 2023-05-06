from flask import Blueprint, render_template, redirect, url_for, request, flash, current_app
from .services import getAllFlowersService, getAFlowerByIDService, postAFlowerService, updateAFlowerService, deleteAFlowerService

Flowers = Blueprint("Flowers", __name__)

#API lấy tất cả thông tin hoa
@Flowers.route("/getAllFlowers", methods = ['GET'])
def getAllFlowers():
    return getAllFlowersService()

#api lấy thông tin hoa theo id
@Flowers.route('/getAFlower/<flowerID>', methods = ['GET'])
def getAFlowerByID(flowerID):
    return getAFlowerByIDService(flowerID)

#api thêm một bông hoa
@Flowers.route("/postAFlower", methods = ['POST'])
def postAFlower():
    return postAFlowerService()

#api cập nhật thông tin hoa
@Flowers.route("/updateAFlower/<flowerID>", methods = ['PUT'])
def updateAFlower(flowerID):
    return updateAFlowerService(flowerID)

#api xóa thông tin hoa
@Flowers.route("/deleteAFlower/<flowerID>", methods = ['DELETE'])
def deleteAFlower(flowerID):
    return deleteAFlowerService(flowerID)