from .extensions import db

class Flowers(db.Model):
    __tablename__ = 'Flowers'
    flowerID = db.Column(db.Integer, primary_key = True)
    flowerTen = db.Column(db.UnicodeText, nullable = False)
    flowerTenKH = db.Column(db.String(50))
    flowerGioi = db.Column(db.String(50))
    flowerBo = db.Column(db.String(50))
    flowerHo = db.Column(db.String(50))
    flowerNganh = db.Column(db.String(50))
    flowerLop = db.Column(db.String(50))
    flowerMota = db.Column(db.UnicodeText)
    flowerDacdiem = db.Column(db.UnicodeText)
    flowerNoipb = db.Column(db.UnicodeText)

    def __init__(self, flowerTen, flowerTenKH, flowerGioi, flowerBo, flowerHo, flowerNganh, flowerLop, flowerMota, flowerDD, flowerNoiss):
        self.flowerTen = flowerTen
        self.flowerTenKH = flowerTenKH
        self.flowerGioi = flowerGioi
        self.flowerBo = flowerBo
        self.flowerHo = flowerHo
        self.flowerNganh = flowerNganh
        self.flowerLop = flowerLop
        self.flowerMota = flowerMota
        self.flowerDacdiem = flowerDD
        self.flowerNoipb = flowerNoiss

class Admin(db.Model):
    __tablename__ = 'Admin'
    adminID = db.Column(db.Integer, primary_key = True)
    adminUN = db.Column(db.String, nullable = False)
    adminPw = db.Column(db.String, nullable = False)

    def __init__(self, adminUN, adminPw):
        self.adminUN = adminUN
        self.adminPw = adminPw

class Log(db.Model):
    __tablename__ = 'Log'
    logID = db.Column(db.Integer, primary_key = True)
    adminID = db.Column(db.Integer, db.ForeignKey("Admin.adminID"))
    flowerID = db.Column(db.Integer)
    message = db.Column(db.UnicodeText, nullable = False)

    def __init__(self, adminID, flowerID, message):
        self.adminID = adminID
        self.flowerID = flowerID
        self.message = message