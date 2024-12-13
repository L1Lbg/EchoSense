import sys
import os
def renamefilefolder(filefolder, new_name):
    try:
        os.rename(filefolder, new_name)
    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé"), False
    except PermissionError:
        print("Vous n'avez pas les permissions pour changer ce fichier."), False
    except Exception as e:
        print("Une erreur inconnue est survenue lors du changer de nom du fichier"), False

    return "Fichier renomé correctement", True

if __name__ == "__main__":
    renamefilefolder(sys.argv[1],sys.argv[2])