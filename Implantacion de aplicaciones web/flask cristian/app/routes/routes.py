from flask import Blueprint, render_template, request

from app import db
from app.data.mazo_dao import MazoDao


rutas_usuarios = Blueprint("routes", __name__)




@rutas_usuarios.route('/')
def ver_mazos():
    mazo_dao = MazoDao()
    mazos = mazo_dao.select_all(db)
    return render_template('index.html',mazos=mazos)