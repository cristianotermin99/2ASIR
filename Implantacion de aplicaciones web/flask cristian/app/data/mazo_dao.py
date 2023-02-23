from app.data.modelo.mazo import Mazo
from sqlalchemy.orm import Session
import mysql.connector

class MazoDao:
    def __init__(self, session: Session):
        self.session = session

    def select_all(self,db) -> list[Mazo]:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM mazo')
        mazos_en_db = cursor.fetchall()
        mazos : list[Mazo]= list()
        for mazo_en_db in mazos_en_db:
            mazos.append(Mazo(mazo_en_db[0], mazo_en_db[1]))
        cursor.close()
        return mazos

    def add_mazo(self,db, mazo : Mazo):
        resultado=""
        cursor = db.cursor()
        sql = "INSERT INTO mazo VALUES (%s,%s)"
        datos=(mazo.nombre, mazo.descripcion)
        try:
            cursor.execute(sql,datos)
            db.commit()  #importar el mysql connector
            resultado="valido"
        except:
            db.rollback()
            resultado="no valido"
        cursor.close()
        return resultado
