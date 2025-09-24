class Article:
    def __init__(self, id, reference, designation, stock, pmp):
        self.id = id
        self.reference = reference
        self.designation = designation
        self.stock = stock
        self.pmp = pmp

    def __repr__(self):
        return f"<Article {self.reference} - {self.designation} (Stock: {self.stock}, PMP: {self.pmp})>"
