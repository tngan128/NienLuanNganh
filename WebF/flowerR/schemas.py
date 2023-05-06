from .extensions import ma

class FlowerSchema(ma.Schema):
    class Meta:
        fields = ('flowerID', 'flowerTen', 'flowerTenKH', 'flowerGioi', 'flowerBo', 'flowerHo', 'flowerNganh', 'flowerLop', 'flowerMota', 'flowerDacdiem', 'flowerNoipb')

class AdminSchema(ma.Schema):
    class Meta:
        fields  = ('adminID', 'adminUN', 'adminPw')

class LogSchema(ma.Schema):
    class Meta:
        fields  = ('logID', 'adminID', 'flowerID', 'message')