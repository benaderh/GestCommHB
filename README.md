# GestCommHB

Gestion commerciale de pièces de rechange pour véhicules (achats, ventes, stocks, valorisation PMP) avec base de données locale SQLite et interface graphique PyQt5.

## Fonctionnalités principales
- Gestion des articles (pièces de rechange)
- Achats et ventes
- Gestion des stocks
- Valorisation des stocks en Prix Moyen Pondéré (PMP)
- Interface graphique moderne

## Installation

1. Cloner le dépôt ou copier le dossier sur votre PC.
2. Installer les dépendances Python :
   ```bash
   pip install -r requirements.txt
   ```
3. Initialiser la base de données :
   ```bash
   python gestcommhb/database/db.py
   ```
4. Lancer l’application :
   ```bash
   python gestcommhb/ui/main_window.py
   ```

## Structure du projet
- `gestcommhb/database/` : gestion de la base SQLite
- `gestcommhb/models/` : modèles de données (Article, Achat, Vente)
- `gestcommhb/controllers/` : logique métier (achats, ventes, stocks)
- `gestcommhb/ui/` : interface graphique PyQt5

## Auteurs
- Votre nom ici