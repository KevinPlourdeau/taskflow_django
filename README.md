# TaskFlow — Application de gestion de tâches avec Django

## Présentation

TaskFlow est un projet personnel développé pour enrichir mon portfolio de développeur junior.

L’objectif est de créer une application web simple et propre permettant de gérer des tâches du quotidien avec un système CRUD complet (Create, Read, Update, Delete).

Ce projet me permet de démontrer ma compréhension des bases du développement backend avec Django, la gestion des modèles, des vues, des templates et de la base de données.

---

## Objectifs du projet

* Comprendre la structure d’un projet Django
* Mettre en place un CRUD complet
* Gérer une base de données avec Django ORM
* Créer une interface web simple et fonctionnelle

---

## Fonctionnalités

### Gestion des tâches

* Ajouter une tâche
* Modifier une tâche
* Supprimer une tâche
* Consulter la liste des tâches

### Statuts disponibles

* À faire
* En cours
* Terminée

### Dashboard simple

* Nombre total de tâches
* Nombre de tâches terminées
* Nombre de tâches en cours

---

## Stack technique

* Python
* Django
* HTML
* CSS
* SQLite
* GitHub

---

## Installation du projet

### 1. Cloner le projet

```bash
git clone URL_DU_REPO
cd taskflow
```

### 2. Installer Django

```bash
pip install django
```

### 3. Appliquer les migrations

```bash
python manage.py migrate
```

### 4. Lancer le serveur

```bash
python manage.py runserver
```

### 5. Ouvrir dans le navigateur

```txt
http://127.0.0.1:8000/
```

---

## Structure du projet

```txt
taskflow/
├── manage.py
├── db.sqlite3
├── taskflow/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── tasks/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
└── templates/
```

---

## Améliorations futures

* Authentification utilisateur
* Catégories de tâches
* Date limite
* Priorités
* Recherche et filtres
* Migration vers PostgreSQL
* Dockerisation du projet

---

## Auteur

Projet réalisé par Kevin dans le cadre de l’enrichissement de mon portfolio développeur web et backend.
