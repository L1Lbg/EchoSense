# https://pypi.org/project/appopener/
from AppOpener import open
import sys
def openapp(app_name):
    try:
        open(app_name, throw_error=True, match_closest=True, output=True)
    except Exception as e:
        if 'is not running' in str(e): 
            return "L'application spécifiée n'existe pas.", False

    return "L'application à été ouverte correctement", True

if __name__ == "__main__":
    openapp(sys.argv[1])