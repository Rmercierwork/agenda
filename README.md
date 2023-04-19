# Mon Agenda

Mon Agenda est une application web qui permet de gérer vos contacts et de planifier des rendez-vous.

## Prérequis

- Python 3.8 ou supérieur
- Pip (Gestionnaire de paquets Python)
- PostgreSQL

## Installation

1. Clonez ce dépôt dans un répertoire de votre choix :
https://github.com/Rmercierwork/agenda.git
2. Accédez au répertoire du projet :
`cd agenda_raphael` -> `cd my_agenda`
3. Créez un environnement virtuel et activez-le :
`python -m venv venv`
`venv\Scripts\activate`
4. Installez les dépendances du projet :
`pip install -r requirements.txt`
5. Configurez les variables d'environnement pour la base de données et les autres paramètres requis. Par exemple, créez un fichier `.env` dans le répertoire du projet avec le contenu suivant (remplacez les valeurs par celles de votre configuration) :
SECRET_KEY=your_secret_key_here
DEBUG=True
DATABASE_URL=postgres://user:password@localhost/dbname

6. Effectuez les migrations de la base de données :
`python manage.py migrate`

## Utilisation

1. Lancez le serveur de développement :
`python manage.py runserver`

2. Ouvrez un navigateur et accédez à l'application à l'adresse `http://127.0.0.1:8000/`.



