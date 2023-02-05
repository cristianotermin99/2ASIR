from app.data.modelo.carta import Carta

class CartasDao:

    def select_all(self,db) -> list[Carta]:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM cartas')
        cartas_en_db = cursor.fetchall()
        cartas : list[Carta]= list()
        for carta_en_db in cartas_en_db:
            cartas.append(Carta(carta_en_db[0], carta_en_db[1], carta_en_db[2],carta_en_db[3]))

        cursor.close()
        return cartas