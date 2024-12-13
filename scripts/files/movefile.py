import shutil
import sys

def movefile(from_src, to):
    try:
        shutil.move(from_src, to)
    except FileNotFoundError:
        return "Le ficher que vous avez specifié n'existe pas.", False
    except PermissionError as e:
        return "Vous n'avez pas la permission de bouger ces fichiers.", False
    except Exception as e:
        return "Une erreur inattendue s'est produite.", False
    
    return "Le fichier a été bougé correctement.", True
    

if __name__ == "__main__":
    movefile(sys.argv[1], sys.argv[2])