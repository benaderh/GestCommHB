from gestcommhb.database.db import get_connection

class VenteController:
    @staticmethod
    def ajouter_vente(date, article_id, quantite, prix_unitaire):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ventes (date, article_id, quantite, prix_unitaire) VALUES (?, ?, ?, ?)", (date, article_id, quantite, prix_unitaire))
        conn.commit()
        conn.close()
