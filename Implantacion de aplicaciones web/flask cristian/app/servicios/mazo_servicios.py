from sqlalchemy.orm import Session
from app.data.modelo.mazo import Mazo
from app.data.mazo_dao import MazoDao


class Mazo_servicios:
    def __init__(self, db):
        self.mazo_dao = MazoDao(db)
        self.model = Mazo

    def select_all(self,db):
        return self.mazo_dao.select_all(db)

    def add_mazo(self,db, mazo:Mazo):
        return self.mazo_dao.add_mazo(db,mazo)
    