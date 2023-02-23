from app.data.modelo.carta import Carta
from sqlalchemy.orm import Session
import mysql.connector

class CartasDao:
    def __init__(self, session: Session):
        self.session = session

    def select_all(self,db, mazo:str) -> list[Carta]:
        cursor = db.cursor()
        sql='SELECT * FROM cartas WHERE nombre_mazo='+'"'+mazo+'"'
        cursor.execute(sql)
        cartas_en_db = cursor.fetchall()
        cartas : list[Carta]= list()
        for carta_en_db in cartas_en_db:
            cartas.append(Carta(carta_en_db[0], carta_en_db[1], carta_en_db[2],carta_en_db[3]))
        cursor.close()
        return cartas

    