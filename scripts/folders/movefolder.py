import os
import shutil
def movefolder(src_folder, dest_folder):
    if not os.path.exists(dest_folder):
       return "Le dossier de destination n'existe pas."
    try:
        shutil.move(src_folder, dest_folder)
    except PermissionError:
        return "Permission refusée pour déplacer le dossier.", False
    except:
        return "Erreur inconnue lors de la tentative de déplacement du dossier.", False
    
    return "Le dossier a été bougé correctement.", True