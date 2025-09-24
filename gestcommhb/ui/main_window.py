import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QTabWidget, QWidget, QVBoxLayout, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Gestion Commerciale - Pièces de Rechange')
        self.setGeometry(100, 100, 900, 600)
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.init_menu()
        self.init_tabs()

    def init_menu(self):
        menubar = self.menuBar()
        fichier = menubar.addMenu('Fichier')
        quitter = QAction('Quitter', self)
        quitter.triggered.connect(self.close)
        fichier.addAction(quitter)

    def init_tabs(self):
        self.tabs.addTab(QLabel('Tableau de bord'), 'Accueil')
        self.tabs.addTab(QLabel('Gestion des articles'), 'Articles')
        self.tabs.addTab(QLabel('Achats'), 'Achats')
        self.tabs.addTab(QLabel('Ventes'), 'Ventes')
        self.tabs.addTab(QLabel('Stocks'), 'Stocks')
        self.tabs.addTab(QLabel('Valorisation PMP'), 'Valorisation PMP')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
