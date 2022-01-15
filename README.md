# change-manager

Interface graphique en Python pour gérer les connexions sur les serveurs dans le cadre de la gestion des changement avec GLPI.
L'interface permet de demander à l'utilisateur différentes informations, de lui faire valider les conditions d'accès et de soit créer une nouvelle demande de changement via l'API de GLPI, soit de sélectionner un changement déjà existant.

# pré requis
Installer les dépendances suivantes : 

- pip install configparser
- pip install requests
- pip install unidecode
- pip install cryptography

# Eléments fonctionnels
- Ouverture d'une fenêtre en plein écran, sans possibilité de la fermer.
- Formulaire d'identité + envoi d'un mail au support + création d'un nouveau changement dans GLPI
- Lecture des conditions d'utilisation
- Accès en urgence (bypass)
- Stockage des clé API avec chiffrement (efficacité de la sécurité à valider)

# Eléments non fonctionnels ou à mettre en place
- Lister les changements déjà ouvert en fonction d'un nom d'utilisateur
- Renseigner un numéro de changement
