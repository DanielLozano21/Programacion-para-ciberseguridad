try: 
    import requests

except ImportError: 
    os.system('pip install requests') 
    print('Installing requests...') 
    print('Ejecuta de nuevo tu script...') 
    exit() 

try: 
    import os

except ImportError: 
    os.system('pip install os') 
    print('Installing os...') 
    print('Ejecuta de nuevo tu script...') 
    exit() 

try: 
    import os

except ImportError: 
    os.system('pip install os') 
    print('Installing os...') 
    print('Ejecuta de nuevo tu script...') 
    exit()

try: 
    import sys

except ImportError: 
    os.system('pip install sys') 
    print('Installing sys...') 
    print('Ejecuta de nuevo tu script...') 
    exit()

try:
    import webbrowser

except ImportError:
    os.system('pip install webbrowser')
    print('Installing webbrowser...')
    print('Ejecuta de nuevo tu script...')
    exit()

try:
    from bs4 import BeautifulSoup as bs

except ImportError:
    os.system('pip install BeautifulSoup')
    print('Installing BeautifulSoup...')
    print('Ejecuta de nuevo tu script...')
    exit()

"""Daniel Adrian Lozano Garza
Las primeras exepciones del programa estan hechas por si no tienes
un modulo instalado, estas lo instalan y continuamente cierran el programa.
Despues continuamos con los input que forman un rango del numero de paginas en
las que se va a buscar y el ultimo te pide las siglas de una facultad para 
poder buscar noticias sobre ella mediante el script.
El primer if valida que este correctamente ordenado rango de las paginas a las
se buscara.
Despues continuamos con un for que hara el mismo procedimiento con cada una de
las paginas a las que se desea investigar, el primer if valida que el estado de
la pagina sea el correcto.
Despues mediante el uso de BeautifulSoap extrae la informacion del url que se
esta buscando y la compara con el tag de la facultad que le dimos para al final
si encuentra alguna coincidencia abrir el url mediante webbrowser."""

print("Este script navega en las páginas de noticas de la UANL")
inicioRango = int(input("Pagina inicial para buscar: "))
finRango = int(input("Pagina final para buscar: "))
dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
if inicioRango > finRango:
    inicioRango,finRango = finRango,inicioRango
for i in range (inicioRango,finRango,1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get (url)
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    else:
        soup = bs(pagina.content,"html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content,"html.parser")
                parrafos = soup2.select("p")    
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print ("Abriendo",url2)
                        webbrowser.open(url2)
                        break
    