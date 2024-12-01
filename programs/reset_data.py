import os
import glob
import json

# Suprime tous les fichier du dossier 'data'
files = glob.glob('data/*')
for f in files:
    os.remove(f)


# vide le tableau de nom des utilisateurs
with open('programs\\utils\\users_names.json', 'w') as json_file:
    json.dump({"users_names": []}, json_file, indent=4)
