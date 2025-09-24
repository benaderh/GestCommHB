from gestcommhb.database.db import get_connection

class AchatController:
    @staticmethod
    def ajouter_achat(date, article_id, quantite, prix_unitaire):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO achats (date, article_id, quantite, prix_unitaire) VALUES (?, ?, ?, ?)", (date, article_id, quantite, prix_unitaire))
        conn.commit()
        conn.close()
