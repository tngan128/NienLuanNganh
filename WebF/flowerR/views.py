from flask import Blueprint, render_template, session

views = Blueprint("views", __name__)

@views.route("/")
def homePage():
    return render_template("index.html")

@views.route("/admin")
def adminPage():
    return render_template("admin.html")

@views.route("/admin/login")
def adminLoginPage():
    return render_template("adminLogin.html")

@views.route("/flowers")
def flowersPage():
    return render_template("flowers.html")

@views.route("/flowers/info")
def flowerInfoPage():
    return render_template("flowerinfo.html")

@views.route("/flowers/add")
def addFlowersPage():
    return render_template("addAFlower.html")

@views.route("/flowers/update")
def updateFlowersPage():
    return render_template("updateFlower.html")

@views.route("/contact")
def contactPage():
    return render_template("contact.html")

@views.route("/recognize")
def recognitionPage():
    return render_template("recognize.html")



