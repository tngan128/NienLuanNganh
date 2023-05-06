from flowerR.extensions import ma, db
from flowerR.schemas import FlowerSchema, LogSchema
from flowerR.model import Flowers, Log
from flask import jsonify, request, session
import traceback

fSchema = FlowerSchema()
fsSchema = FlowerSchema(many=True)
LSchema = LogSchema()


def getAllFlowersService():
    data = Flowers.query.all()
    print(data)
    if data:
        return fsSchema.jsonify(data)
    else:
        return {'message': 'No flower has been found'}


def getAFlowerByIDService(flowerID):
    flower = Flowers.query.get(flowerID)
    if flower:
        return fSchema.jsonify(flower)
    else:
        return {'message': 'No flower has been found for the given ID'}


def postAFlowerService():
    # ghi nhận lại thông tin truyền vào từ người dùng
    flowerTen = request.json['flowerTen']
    flowerTenKH = request.json['flowerTenKH']
    flowerGioi = request.json['flowerGioi']
    flowerBo = request.json['flowerBo']
    flowerHo = request.json['flowerHo']
    flowerNganh = request.json['flowerNganh']
    flowerLop = request.json['flowerLop']
    flowerMota = request.json['flowerMota']
    flowerDacdiem = request.json['flowerDacdiem']
    flowerNoipb = request.json['flowerNoipb']

    try:
        newFlower = Flowers(flowerTen, flowerTenKH, flowerGioi, flowerBo, flowerHo,
                            flowerNganh, flowerLop, flowerMota, flowerDacdiem, flowerNoipb)
        if 'adminID' in session:
            newflowerID = Flowers.query.order_by(Flowers.flowerID.desc()).first().flowerID + 1
            newLog = Log(session['adminID'], newflowerID, "Add a new Flower")
            db.session.add(newLog)
        db.session.add(newFlower)
        db.session.commit()
        return fSchema.jsonify(newFlower)
    except:
        print(traceback.format_exc())
        return {'message': "Unsuccessful adding"}, 404


def updateAFlowerService(flowerID):
    flower = Flowers.query.get(flowerID)
    if not flower:
        return {'message': "Unsuccessful deleting"}, 404
    flower.flowerTen = request.json['flowerTen']
    flower.flowerTenKH = request.json['flowerTenKH']
    flower.flowerGioi = request.json['flowerGioi']
    flower.flowerBo = request.json['flowerBo']
    flower.flowerHo = request.json['flowerHo']
    flower.flowerNganh = request.json['flowerNganh']
    flower.flowerLop = request.json['flowerLop']
    flower.flowerMota = request.json['flowerMota']
    flower.flowerDacdiem = request.json['flowerDacdiem']
    flower.flowerNoipb = request.json['flowerNoipb']
    if 'adminID' in session:
        newLog = Log(session['adminID'], flowerID, "update a Flower")
        db.session.add(newLog)
    db.session.commit()
    return {'message': "Successfully delete"}


def deleteAFlowerService(flowerID):
    flower = Flowers.query.get(flowerID)
    if flower:
        if 'adminID' in session:
            newLog = Log(session['adminID'], flowerID, "delete a Flower")
            db.session.add(newLog)
        db.session.delete(flower)        
        db.session.commit()
        return {'message': "Successfully delete"}, 204
    else:
        return {'message': "Unsuccessfully delete"}, 404
