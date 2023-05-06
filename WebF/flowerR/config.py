import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.environ.get("Key")
SESSION_TYPE = 'filesystem'
SESSION_REFRESH_EACH_REQUEST = False
path = os.path.dirname(__file__)
UPLOAD_FOLDER = path + os.environ.get("uf")



DLMODEL = path + os.environ.get("modelPath")
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")