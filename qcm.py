import json
import csv
import os
from datetime import datetime # pour date et heure

# Gestion des Utilisateurs
utilis_fichier = "utilisateurs.json"
question_fichier = "questions.json"

#recuperer les users de json  et retourner ces donnes 
def recup_utilisateur():
    if os.path.exists(utilis_fichier):  #Verifie si le fichier utilisateurs.json existe
        with open(utilis_fichier, "r") as file:
            return json.load(file)  # convertir des fichiers JSON en objets Python recuperer les donner de json en python
    return {}

#écrire les données dans le fichier utilisateurs.json
def sauvegarde_utilisateur(utilisateur):
    with open(utilis_fichier, "w") as file: #Si le fichier utilisateurs.json n'existe pas encore, Python le cree automatiquement en mode ecriture ("w") sinon l'ouvrire seulement en mode ecriture
        json.dump(utilisateur, file) # convertir un utilisateur de Python en JSON et l'écrire directement dans fichier utilisateurs.json.



def get_or_create_user():
    utilisateur = recup_utilisateur()
    username = input("Entrez votre nom d'utilisateur : ")

    if username in utilisateur: #si usernaame existe dans fichier utilisateurs.json in affiche son historique(date+score)
        print(f"Bienvenue de retour, {username}! Voici votre historique :")
        for his in utilisateur[username]["history"]:
            print(f"- [La Date: {his['date']}, Votre Score: {his['score']}")
    else:  
        print(f"Bienvenue, {username}! Un nouveau profil a été créé.")
        utilisateur[username] = {"history": []}
        sauvegarde_utilisateur(utilisateur)

    return username, utilisateur


# Gestion des Questions

def load_questions():
    if os.path.exists(question_fichier):
        with open(question_fichier, "r") as file:
            return json.load(file)
    else:
      print("Le fichier de questions est introuvable !")


def select_category(questions):
    print("Catégories disponibles :")
    categories = list(questions.keys())
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")

    choice = int(input("Choisissez une catégorie : ")) - 1
    return categories[choice]