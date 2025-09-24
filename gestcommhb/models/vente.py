class Vente:
    def __init__(self, id, date, article_id, quantite, prix_unitaire):
        self.id = id
        self.date = date
        self.article_id = article_id
        self.quantite = quantite
        self.prix_unitaire = prix_unitaire

    def __repr__(self):
        return f"<Vente {self.id} Article:{self.article_id} Qte:{self.quantite} PU:{self.prix_unitaire}>"
