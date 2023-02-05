
from app.data.modelo.mazo import Mazo

class MazoDao:

    def select_all(self,db) -> list[Mazo]:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM mazo')
        mazos_en_db = cursor.fetchall()
        mazos : list[Mazo]= list()
        for mazo_en_db in mazos_en_db:
            mazos.append(Mazo(mazo_en_db[0], mazo_en_db[1]))
        cursor.close()
        return mazos

    def add_mazo(self,db, nombre : str, descripcion : str):
        cursor = db.cursor()
        sql = "INSERT INTO mazo VALUES (%s,%s)"
        datos=(nombre, descripcion)
        cursor.execute(sql,datos)
        
        return mazo