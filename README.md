# Index
petit projet pour le cours d'indexation web ENSAI 3A SID fait par Thomas Hilger. Le but est de coder un index non-positionnel.

## Quickstart 
Pour créer un index, il suffit de lancer à la racine du projet la commane `python main.py`. L'index nouvellement créer se trouvera dans le fichier json `title.non_pos_index.json`. De plus un fichier avec quelques résultats statistiques sera produit.

Pour lancer les tests, déplacez-vous dans le dossier test, puis lancez la commande `pytest`.

## Explication 

L'index est codé dans la classe index. les grandes étapes sont :

pour chaque url on effecute:
    - on requête l'url
    - on récupère le titre du document
    - on tokenise le titre. Tous les tokens sont stockés dans un dictionnaire où l'on retrouve pour chaque document le nombre de fois où le token apparaît dans le titre du document. 


