# Exercice Django

Cette application web est composée d'un back-end Django, un front-end HTML/CSS.
Elle permet de créer des articles si l'on est connecté.
On peut consulter les articles librement et trier les articles en fonction de tags. (Ils sont triés par date de création par défaut)
En tant qu'administrateur on peut supprimer ou modifier les articles.

## Administrateur
Un utilisateur administrateur existe déjà, il suffit de se connecter avec:

admin
adminpassword

## Utilisateur
Un utilisateur lambda existe également:

```python
lambdaUser
lambaPassword
```
On peut aussi créer un nouvel utilisateur lambda à partir de l'application dans l'onglet inscription.

## Installation

Pour exécuter l'application il faut lancer la commande suivante:

```bash
cd djangonautic
python manage.py runserver
```

