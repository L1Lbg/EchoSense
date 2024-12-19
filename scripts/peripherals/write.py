import pyautogui

def write(content):
    pyautogui.write(content)

if __name__ == '__main__':
    write(str(input('Contenu a écrire:\n')))