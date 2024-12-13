import psutil

def performancestats():
    return f"""
        Le pourcentage de la mémoire utilisée est de {psutil.virtual_memory().percent}%
        Le pourcentage du processeur utilisé est de {psutil.cpu_percent(interval=1)}%
    """, True


if __name__ == '__main__':
    print(performancestats())