# projet algo steam shop

.\env\requirement.txt >>> liste pip

".\env\Scripts\activate" >>> active le venv

"python manage.py runserver" >>> lance le site web, a faire depuis ".\project\"

[text](http://127.0.0.1:8000/admin/)
admin login :
    id : admin 
    mdp : admin


répartion du travail :

-Mathieu le du de jesus : gestion du github, backend django
-Mattieu Charier : html, css
-Nathan Tereszkiewicz : ajout des jeux, conseils ux design

participation commune sur le readme.md

django :

    dossier steam shop : 
        dossier de base du projet django
    
    fichier manage.py :
        permet de faire les commandes des base de django tel que runserver, makemigrations, migrate...

    db.sqlite3 : 
        base de donnée du site

    application account : 
        definit la class userB, et gere les signup, login et logout

    application store : 
        definit les class product, order et cart dans models.py et gere la logique et le backend des pages web dans views.py

    dossiers templates : 
        contiennent les fichiers html
    
    dossier média : 
        contient les images relatives au produits
    
