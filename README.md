# SpaceX Falcon 9 First Stage Landing Prediction — IBM Applied Data Science Capstone

Projet final : prédire si le premier étage du Falcon 9 atterrit avec succès, afin d'estimer le coût d'un lancement
(SpaceX : 62 M$ contre 165 M$ et plus chez les concurrents, grâce à la réutilisation du premier étage).

**Auteur** : Vigninou Gédéon Akponon

## Contenu du dépôt

| Étape | Fichier | Description |
|---|---|---|
| 1. Collecte (API) | `spacex-data-collection-corrige.ipynb` | Requêtes à l'API SpaceX, construction du jeu de données Falcon 9 |
| 2. Collecte (web scraping) | `jupyter-labs-webscraping-corrige.ipynb` | Extraction du tableau des lancements sur Wikipédia (BeautifulSoup) |
| 3. Nettoyage / Data wrangling | `labs-jupyter-spacex-Data_wrangling-corrige.ipynb` | Valeurs manquantes, création de la variable cible `Class` |
| 4. EDA avec visualisation | `edadataviz-corrige.ipynb` | Graphiques (dispersion, barres, tendance annuelle), variables indicatrices |
| 5. EDA avec SQL | `jupyter-labs-eda-sql-corrige.ipynb` | 10 requêtes SQL sur les lancements (SQLite) |
| 6. Carte interactive | `spacex-folium-map.ipynb` | Carte Folium : sites, succès/échecs, distances de proximité |
| 7. Tableau de bord | `spacex_dash_app.py` | Application Plotly Dash (liste déroulante, camembert, curseur, nuage de points) |
| 8. Prédiction | `SpaceX_Machine_Learning_Prediction_Part_5-corrige.ipynb` | Régression logistique, SVM, arbre de décision, KNN, matrice de confusion |

## Exécuter le tableau de bord

```bash
python3 -m pip install pandas dash
wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"
python spacex_dash_app.py   # puis ouvrir http://127.0.0.1:8050
```

## Technologies
Python, pandas, NumPy, requests, BeautifulSoup, SQLite, Matplotlib, Seaborn, Folium, Plotly Dash, scikit-learn.
