import json
import os

def find_next_id():
    """
    Trouve le prochain id de la personne suivante 
    """
    last_id = 0
    path = 'data'
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]

    for imagePath in imagePaths :
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        if id > last_id :
            last_id = id
    return last_id + 1


def get_user_name():
    """
    Avoir le user name du sample vérifier qu'il n'est pas déja utilisé. Ensuite le sauver dans le fichier
    """

    with open('users_names.json', 'r') as file:
        users_names = json.load(file)

    while True:
            user_name = input('\nEnter user name: ').strip()

            if user_name not in users_names["users_names"]:
                # Ajouter le nouveau nom
                users_names["users_names"].append(user_name)

                # Sauvegarder le fichier
                with open('users_names.json', 'w') as json_file:
                    json.dump(users_names, json_file, indent=4)

                print("User ajouté :", user_name)
                break
            else:
                print("Ce nom existe déjà. Veuillez essayer un autre.")
        
    return user_name