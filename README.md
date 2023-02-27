# Master

[![forthebadge](http://forthebadge.com/images/badges/powered-by-electricity.svg)](https://github.com/mikailsupdevinci)

Une petite description du projet

## Pour commencer

Cette branch "Master" est conçu pour pouvoir effectuer le fichier Jenkinsfile depuis notre Jenkins qui est stocké sur notre docker.
Il contient entre autre notre projet backend qui est "app.py".
Tout ça a été effectué sur une machine Windows.

### Pré-requis

- Docker Desktop
- Editeur de code (Vscode par exemple)
- Jenkins 

### Installation

Tout d'abord, il faudra le projet frontend ainsi que le projet backend.
Le front se trouve https://github.com/raoufcherfa/Imad-aws dans le dossier angular.

Une fois le dossier angular récupéré, il faudra le backend, ici le backend a été écrit via python qui est le fichier app.py.

Avant de créer une image docker, il faut exécuter la commande ``wsl --update`` pour pouvoir créer un environnement linux et pouvoir utiliser docker convenablement.

Maintenant, il faut exécuter via un terminal la commande suivante : ``docker build -t "nom de l'image"`` . Dans le dossier ou se trouve le frontend (angular) et le backend qui est dans cette branche.
Cela va créer une image docker et ensuite pour pouvoir exécuter l'image, il faut la mettre en container tous sur le port 80.

Une fois les containers réalisés, tester le front et le back si tout fonctionne correctement.

Si les test sont OK, il faut télécharger le JenkinsFile via ce github : https://github.com/raoufcherfa/employe
Une fois le fichier téléchargé, il faudra installer jenkins tout se trouve sur leur site officiel : https://www.jenkins.io/download/
Une fois jenkins installé et déployé sur votre machine docker, il faudra utiliser le jenkinsfile précedemment pour pouvoir effectuer les tests.

Vous allez être bloqué à l'étape du build si votre code est bon si ce n'est pas le cas revoyez votre code. Pour passer l'erreur Build, il faudra exécuter les commandes suivantes : 

``docker exec -it -u 0 “ID de container” /bin/bash
apt-get update / apt-get upgrade
apt-get install python3
apt-get install pip
pip install pytest``

Vous devriez obtenir ceci : 
![image](# Master

[![forthebadge](http://forthebadge.com/images/badges/powered-by-electricity.svg)](https://github.com/mikailsupdevinci)

Une petite description du projet

## Pour commencer

Cette branch "Master" est conçu pour pouvoir effectuer le fichier Jenkinsfile depuis notre Jenkins qui est stocké sur notre docker.
Il contient entre autre notre projet backend qui est "app.py".
Tout ça a été effectué sur une machine Windows.

### Pré-requis

- Docker Desktop
- Editeur de code (Vscode par exemple)
- Jenkins 

### Installation

Tout d'abord, il faudra le projet frontend ainsi que le projet backend.
Le front se trouve https://github.com/raoufcherfa/Imad-aws dans le dossier angular.

Une fois le dossier angular récupéré, il faudra le backend, ici le backend a été écrit via python qui est le fichier app.py.

Avant de créer une image docker, il faut exécuter la commande ``wsl --update`` pour pouvoir créer un environnement linux et pouvoir utiliser docker convenablement.

Maintenant, il faut exécuter via un terminal la commande suivante : ``docker build -t "nom de l'image"`` . Dans le dossier ou se trouve le frontend (angular) et le backend qui est dans cette branche.
Cela va créer une image docker et ensuite pour pouvoir exécuter l'image, il faut la mettre en container tous sur le port 80.

Une fois les containers réalisés, tester le front et le back si tout fonctionne correctement.

Si les test sont OK, il faut télécharger le JenkinsFile via ce github : https://github.com/raoufcherfa/employe
Une fois le fichier téléchargé, il faudra installer jenkins tout se trouve sur leur site officiel : https://www.jenkins.io/download/
Une fois jenkins installé et déployé sur votre machine docker, il faudra utiliser le jenkinsfile précedemment pour pouvoir effectuer les tests.

Vous allez être bloqué à l'étape du build si votre code est bon si ce n'est pas le cas revoyez votre code. Pour passer l'erreur Build, il faudra exécuter les commandes suivantes : 

``docker exec -it -u 0 “ID de container” /bin/bash
apt-get update / apt-get upgrade
apt-get install python3
apt-get install pip
pip install pytest``

Vous devriez obtenir ceci : 
![image](https://user-images.githubusercontent.com/125256971/221597356-0e3f8801-9132-49b8-b77f-edfb907b770d.png))

Il y a aussi le github CI/CD, il faut configurer le fichier yml ( j'ai pris le votre) et lancer. 
![image](https://user-images.githubusercontent.com/125256971/221598869-62b94be3-8eb0-494f-b52b-d4e6d195525a.png)

![image](https://user-images.githubusercontent.com/125256971/221598734-2885f635-9f76-46b1-9cae-4f1438cfc72d.png)


## Fabriqué avec

* [VsCode](https://code.visualstudio.com/) - Editeur de code
* [Docker](https://www.docker.com/) - Tester et déployer rapidement des applications à l'aide de conteneurs
* [Jenkins](https://www.jenkins.io/) - Outil open source de serveur d'automatisation
* [ChatGPT](https://chat.openai.com/) - Agent conversationnel utilisant l'intelligence artificielle

## Versions
Le projet étant un projet débutant, le versionning n'est pas considéré.

## Auteurs
Listez le(s) auteur(s) du projet ici !
* **Mikail ALBAYRAK** _alias_ [@regnat0r](https://github.com/mikailsupdevinci)
[Raouf CHERFA](https://github.com/raoufcherfa/employe) pour voir qui à aidé au projet !)

## Fabriqué avec

* [VsCode](https://code.visualstudio.com/) - Editeur de code
* [Docker](https://www.docker.com/) - Tester et déployer rapidement des applications à l'aide de conteneurs
* [Jenkins](https://www.jenkins.io/) - Outil open source de serveur d'automatisation
* [ChatGPT](https://chat.openai.com/) - Agent conversationnel utilisant l'intelligence artificielle

## Versions
Le projet étant un projet débutant, le versionning n'est pas considéré.

## Auteurs
Listez le(s) auteur(s) du projet ici !
* **Said Abdallah Said Toihir**
[Raouf CHERFA](https://github.com/raoufcherfa/employe) pour voir qui à aidé au projet !
