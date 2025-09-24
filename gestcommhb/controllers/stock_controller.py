from gestcommhb.database.db import get_connection

class StockController:
    @staticmethod
    def get_all_articles():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, reference, designation, stock, pmp FROM articles")
        articles = cursor.fetchall()
        conn.close()
        return articles

    @staticmethod
    def update_stock(article_id, quantite, pmp):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE articles SET stock = stock + ?, pmp = ? WHERE id = ?", (quantite, pmp, article_id))
        conn.commit()
        conn.close()
