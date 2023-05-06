from flowerR.extensions import ma, db
from flowerR.schemas import AdminSchema
from flowerR.model import Admin
from flask import jsonify, request, session, current_app, after_this_request
import traceback

AdSchema = AdminSchema()
AdsSchema = AdminSchema(many=True)


def adminLogin():
    adminUN = request.json['adminUN']
    adminPw = request.json['adminPw']
    if not adminUN or not adminPw:
        return {'message': "Missing Params!"}, 400
    else:
        admin = Admin.query.filter_by(adminUN=adminUN).first()
        if not admin:
            return {'message': "No account has found!"}, 401
        else:
            if adminPw == admin.adminPw:
                session['adminID'] = admin.adminID
                session['adminUN'] = admin.adminUN
                print(session)
                print(current_app.config)
                return {'message': "Successful login"}, 200
            else:
                return {'message': "Wrong password!"}, 401
            
def adminLogout():
    session.pop('adminID', None)
    session.pop('adminUN', None)
    return {'message': "Successful login"}, 200