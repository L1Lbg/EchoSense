import os
def delete_file(filename):
    if os.path.isfile(filename):
        try:
            os.remove(filename)
        except PermissionError:
            return f"Permission refusée pour supprimer le fichier", False
        except:
            return "Erreur inconnue lors de la suppression du fichier", False
    else:
        return "Le fichier spécifié n'existe pas.", False

    return "Le fichier à été supprimé correctement.", True