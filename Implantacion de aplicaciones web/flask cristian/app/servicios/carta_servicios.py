from app.data.modelo.carta import Carta
from app.data.carta_dao import CartasDao
class CartasServicios:
    def __init__(self, db):
        self.cartas_dao = CartasDao(db)
        self.model = Carta
    def select_all(self,db, mazo : str):
        return self.cartas_dao.select_all(db,mazo)