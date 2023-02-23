from flask import Blueprint, render_template, request
from sqlalchemy.orm import Session

from app import db
from app.data.mazo_dao import MazoDao
from app.servicios.mazo_servicios import Mazo_servicios
from app.servicios.carta_servicios import CartasServicios
from app.data.modelo.mazo import Mazo

rutas_usuarios = Blueprint("routes", __name__)




@rutas_usuarios.route('/')
def ver_mazos():
    mazo_servicios = Mazo_servicios(db)
    mazos = mazo_servicios.select_all(db)
    return render_template('index.html',mazos=mazos)

@rutas_usuarios.route("/insert", methods=["POST"])
def add_mazo():
    mazo_servicios = Mazo_servicios(db)
    name = request.form["name"] #coge el vaalor de un campo del form (name)
    descripcion = request.form["descripcion"]
    mazo = Mazo(name,descripcion)
    mazo_servicios.add_mazo(db,mazo)
    return ver_mazos()

@rutas_usuarios.route('/cargarMazosCartas', methods=["GET"])
def ver_mazos_cartas():
    mazo_servicios = Mazo_servicios(db)
    mazos = mazo_servicios.select_all(db)
    return render_template('mazos.html',mazos=mazos)

@rutas_usuarios.route('/cargarCartas', methods=["POST"]) #el nombre de la ruta es el mismo que el action del form
def ver_cartas():
    cartas_servicios = CartasServicios(db)
    mazo = request.form["mazos"]
    cartas = cartas_servicios.select_all(db,mazo)
    return render_template('mazos.html',cartas=cartas)
