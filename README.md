# OpenClassrooms Projet 2 BooksToScrape

# Création environnement

1. Pour créer l'environnement, sur terminal : 

`python -m venv <nomenvironnement>`

2. Par la suite, il faut procéder à l'activation de l'environnement, sur terminal:

`source <nomenvironnement>/bin/activate`

3. Installation dépendances, sur terminal:
`pip install -r requirements.txt`

4. Vérification des modules & packages installés, sur terminal:
`pip freeze`

# Execution des scripts
Il y a  quatre scripts distincts concernant chacune des étapes demandées.


## Scraping article 
1. Dans `src/one_book.py`
- Scrap éléments requis 
- Ajout dans liste `page_scrap_list`
- Ecriture fichier CSV

2. Excution du script par 
`python one_book.py`

3. Changement d'article 
- Nécessite le changement de l'url dans l'objet: 
`page_url =`


## Scraping catégorie
1. Dans `src/one_category.py`
- Je liste les URLs de toutes les pages d'une catégorie 
- Import les fonctions de chaque éléments de `one_book.py`
- Ecriture fichier CSV

2. Execution du script par
`python one_category.py`

3. Changement de categorie 
`scrap_category(urlcategory)`

## Scraping toutes catégories
1. Dans `src/all_categories.py`
- Je liste les URLs de toutes les pages de toutes les catégories
- Import de la fonction `scrap_category(urlcategory)` de `one_category.py`
- Ecriture du fichier CSV

2. Execution du script par
`python all_categories.py`

## Scraping de toutes les catégories et téléchargement images
1. Dans `main.py`
- Je liste les URLs des images de tous les articles du site ainsi que le titre
- Téléchargement des images

2. Execution du script par
`python main.py`
