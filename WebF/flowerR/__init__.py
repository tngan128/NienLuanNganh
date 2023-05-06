from flask import Flask, request, Blueprint
from .FRModel.controller import FGModel
from .Flower.controller import Flowers
from .Admin.controller import Admin
from .views import views
from .extensions import ma, db

def createApp(config_file="config.py"):

    app = Flask(__name__) #khởi tạo all


    app.config.from_pyfile(config_file)
    # Session(app)
    db.init_app(app) #khởi tạo CSDLS
    ma.__init__(app) #khởi schema

    #đăng ký model 
    app.register_blueprint(FGModel)
    app.register_blueprint(views)
    app.register_blueprint(Flowers)
    app.register_blueprint(Admin)

    return app