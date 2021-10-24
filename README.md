# KTR-MSC-SS1

Exercice pour test d'admission en MSc Pro - Architecte système réseau et sécurité.

 Dans ma formation (Licence Pro Admin Sys/Réseau), je fais beaucoup de scripting, mais assez peu de programmation réelle, et encore moins d'orienté objet.

Je me suis donc replongé dans le Python et j'ai essayé d'apprendre les bases de la POO en une semaine à côté de mes cours pour cet exercice. Je n'ai malheureusement pas eu le temps de terminer la partie 6.

Le fichier `main.py` permet de tester les différentes étapes de l'exercice.

## Partie 3

Pour la partie 3, il est spécifié qu'il faut créer une interface. Cependant après quelques recherches je me rends compte que les interfaces n'existent pas nativement en python (il faut ajouter un module), et que dans la plupart des cas elles ne sont pas nécessaires.

C'est pourquoi je décide de simplement placer mes fonctions dans un fichier `Movable.py` que j'importe ensuite dans `Characters.py`.

## Partie 5

En utilisant Python comme langage de programmation, il est difficile d'empêcher chevauchement d'une méthode. [C'est également contraire à la philosophie de Python](https://stackoverflow.com/a/3948937).

