TEST TECHNIQUE - Doria HAMMADI

Le point d'entrée du repo est le fichier main.py, qui permet de lancer la data pipeline, 
La pipeline contient les étapes suivantes :

- La data préparation (fichier praparation.py) :  permet de charger les données sources et applique une un nettoyage sur les données. il renvoi le dossier des données nettoyées.

- La data processing (processing.py) : prend en entrée le dossier retourné par l'étape préparation, applique un ensemble de transformation et retourne le fichier json au format 
{atccode-id : title, date, journal, drug} 

#### Execution de code : 

pour executer le script :

1 - Installer les requirement : 
```sh
pip install -r requirements-dev.txt
```
2- Lancer le code : 
```sh
python3 main.py
```
#### Pour aller plus loin : 

 Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il puisse gérer de grosses volumétries de données (fichiers de plusieurs To ou millions de fichiers par exemple) ?
 
- Pour pouvoir traiter des grosses volumétries des données, On peut utiliser des frameworks de traitement parallèle des datèrent frames et des données comme Pyspark ou Hadoop, ou des services cloud comme Dataflow qui vont permettre de paralléliser les traitements.

- Découper les étapes de traitement le plus possible pour avoir des briques parallélisable 


#### SQL Questions : 

Pour les questions de la partie sql, les reponses sont dans le fichier sql_question/requette.sql
