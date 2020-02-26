# Exercice Django

Cette application web est composée d'un back-end Django, un front-end HTML/CSS.
Elle permet de créer des articles si l'on est connecté.
On peut consulter les articles librement et trier les articles en fonction de tags. (Ils sont triés par date de création par défaut)
En tant qu'administrateur on peut supprimer ou modifier les articles.

## Installation

Pour exécuter l'application il faut lancer la commande suivante:

```bash
cd djangonautic
python manage.py runserver
```
Elle nécessite d'avoir python installé sur votre ordinateur, si vous ne l'avez pas, cliquez [ici](https://www.python.org/downloads/).

## Administrateur
Un utilisateur administrateur existe déjà, il suffit de se connecter avec:

```python
admin
adminpassword
```

## Utilisateur
Un utilisateur lambda existe également:

```python
lambdaUser
lambaPassword
```
On peut aussi créer un nouvel utilisateur lambda à partir de l'application dans l'onglet inscription.

## Article
N'importe quel type d'utilisateur peut créer un article. Il est constitué d'un titre, un contenu, un slug créé automatiquement à partir du titre permettant d'accéder à l'article dans l'url, une image et des tags. L'auteur de l'article est également enregistré et affiché sur la liste d'articles.

## Tags
Les articles peuvent être affichés en fonction de leur tag. Il suffit de cliquer sur le tag en question sur un article le contenant. Il y a également les 4 tags les plus utilisés accessibles sur le côté.

## Inscription
On peut créer un nouvel utilisateur dans l'onglet inscription. Ce formulaire est basé uniquement à partir du formulaire d'inscription basique de Django.

## Modification
Un administrateur peut modifier un article créé par n'importe quel utilisateur. Si un administrateur n'est pas connecté au moment de cliquer sur Modifier, l'utilisateur est redirigé vers la page de connexion.

## Suppression
Un administrateur peut supprimer n'importe quel article. L'utilisateur est également redirigé s'il n'est pas administrateur.
