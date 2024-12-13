import shutil

def deletefolder(path):
    try:
        shutil.rmtree(path)
    except PermissionError :
        return "Vous n'avez pas les permissions nécessaires pour supprimer ce dossier.", False
    except:
        return "Une erreur inattendue s'est produite lors de la suppression du dossier.", False

    return "Le dossier a été supprimé correctement.", True