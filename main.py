import os
import subprocess
import time

def main():
    scripts = {
        "1": "create_dataset.py",
        "2": "training.py",
        "3": "face_recongnition.py",
        "4": "reset_data.py"
    }
    
    # afficher les options
    os.system('cls')
    print("Choose which  file to start :")
    for key, script in scripts.items():
        print(f"{key}. {script}")
    
    # lis le choix 
    choice = input(f"Enter a number to start the script :").strip()
    
    if choice in scripts:
        script_to_run = scripts[choice]
        os.system('cls')
        print(f"Start : {script_to_run}")
        
        # Vérifier si le script existe
        if os.path.exists("./programs/" + script_to_run):
            # Exécuter le script
            subprocess.run(["python", "./programs/" + script_to_run])
            time.sleep(1)
            main()
        else:
            print(f"Erreur : the file {script_to_run} does not exist.")
    else:
        main() # nbr existe pas donc relace scpipt

if __name__ == "__main__":
    main()
