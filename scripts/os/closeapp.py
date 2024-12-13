from AppOpener import close
import sys 
def closeapp(app_name):
    try:
        close(app_name, throw_error=True, output=True)
    except Exception as e:
        if 'is not running' in str(e):
            return "L'application que vous voulez fermer n'est pas en cours d'exécution.", False

    return "L'application a été fermée correctement", True

if __name__ == '__main__':
    closeapp(sys.argv[1])