# BadassRadio - Blog & Webradio

Bienvenue sur la nouvelle version de BadassRadio, refaite entièrement en Python avec le framework Django !

Cette version abandonne WordPress/Blogger au profit d'une interface sur-mesure (plus légère, mobile-friendly et rapide), tout en conservant vos couleurs et l'image de fond iconique.

## Fonctionnalités Principales

- **Albums du mois :** Articles avec titre, artiste, texte et pochette.
- **Playlists :**
  - *Classique :* Une liste de lecture basique (Tracks MP3) qui change l'image du lecteur selon le morceau joué.
  - *Musiques de films (Soundtrack) :* Une liste de lecture avec un diaporama d'images (Slideshow) automatique qui défile pendant la lecture.
- **Visualisation musicale :** Un lecteur audio exclusif avec un effet radial réagissant aux fréquences (façon *Milkdrop*), affichable en plein écran.
- **Backoffice (Admin) :** Interface Django très simple et sécurisée pour gérer les musiques et comptes.
- **Connexion Utilisateurs :** Accès restreint pour les auditeurs avec un formulaire de réinitialisation de mot de passe (via administrateur).

---

## 🚀 Comment tester et lancer le site sur votre machine

Voici les étapes à suivre pour installer le site et le tester localement sur votre ordinateur.

### 1. Prérequis

Assurez-vous d'avoir installé **Python 3** sur votre ordinateur (vérifiez avec `python --version` ou `python3 --version`).

### 2. Installation des dépendances

Ouvrez un terminal (invite de commandes) dans ce dossier racine (là où se trouve ce fichier `README.md`) et installez les outils requis (Django et Pillow pour les images) :

```bash
python3 -m pip install django pillow
```
*(Remarque: sur Windows, utilisez `python` ou `py` à la place de `python3`)*

### 3. Préparation de la base de données

La base de données gère les comptes et vos musiques. Pour l'initialiser la première fois, lancez la commande suivante :

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### 4. Création d'un compte Administrateur

Pour pouvoir vous connecter au site et surtout pour ajouter vos musiques, il faut créer un compte "Super Utilisateur" (Administrateur) :

```bash
python3 manage.py createsuperuser
```
L'invite de commande vous demandera :
- Un nom d'utilisateur (ex: `admin`)
- Une adresse email (laissez vide si vous voulez)
- Un mot de passe (il ne s'affichera pas pendant que vous tapez, c'est normal).

### 5. Démarrage du serveur

Pour lancer le site, tapez cette commande :

```bash
python3 manage.py runserver
```

Votre site est maintenant en ligne localement !

### 6. Accéder au site

Ouvrez votre navigateur web et allez sur l'une de ces adresses :

- **Le site public (Lecteur, Playlists) :** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **L'interface d'Administration (Pour ajouter des Playlists) :** [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

> Connectez-vous avec les identifiants administrateurs que vous venez de créer à l'étape 4.

---

## 🛠️ Ajouter des musiques et tester le lecteur

Pour tester le lecteur audio et l'effet "Milkdrop" :

1. Allez dans l'administration : `http://127.0.0.1:8000/admin`
2. Cliquez sur **Playlists** -> *Ajouter (Add)*
3. Remplissez un titre, et choisissez le type de playlist (`Basic Playlist` ou `Movie Soundtrack`).
4. **Si c'est "Basic" :** Descendez dans la page, et ajoutez des "Tracks" avec un fichier Audio (.mp3) et potentiellement une image associée.
5. **Si c'est "Movie" :** Ajoutez des Tracks audio, ET en dessous ajoutez des "Movie Images". Le lecteur fera tourner ces images en boucle de manière automatique pendant la lecture.
6. Sauvegardez et rendez-vous sur le site public pour écouter !
7. Sur le lecteur, cliquez sur **"Toggle Visualizer"** pour voir l'effet de particules qui réagit à la musique.

Bonnes écoutes ! 🎸
