from flask import Blueprint, request, session, after_this_request
from .services import  adminLogin, adminLogout

Admin = Blueprint("Admin", __name__)

#API lấy tất cả thông tin hoa
@Admin.route("/api/admin/login", methods = ['POST'])
def loginAdminAcc():
    return adminLogin()

@Admin.route("/api/admin/logout", methods = ['POST'])
def logoutAdminAcc():
    return adminLogout()