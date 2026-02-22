import requests

# FUENTES CONFIABLES (Repositorios que se actualizan solos)
FUENTES = [
    "https://raw.githubusercontent.com/GuuS-it/IPTV-Latino/master/Lista.m3u",
    "https://raw.githubusercontent.com/marcofbb/iptv/master/latam.m3u",
    "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/ar.m3u" # Canales Argentina
]

# CANALES QUE QUEREMOS PARA EL NICO
# El robot buscará cualquier canal que contenga estas palabras
BUSQUEDA = ["TNT SPORTS", "ESPN PREMIUM", "TUDN", "FOX SPORTS", "WIN SPORTS"]

def ejecutar():
    lista_final = []
    print("Iniciando recolección de canales...")

    for url in FUENTES:
        try:
            print(f"Buscando en: {url}")
            r = requests.get(url, timeout=15)
            lineas = r.text.split('\n')
            
            for i in range(len(lineas)):
                # Si encontramos un nombre de los que buscamos
                if any(palabra in lineas[i].upper() for palabra in BUSQUEDA):
                    # Guardamos la línea del nombre y la línea del link (que es la siguiente)
                    if i + 1 < len(lineas):
                        lista_final.append(lineas[i]) # La info del canal (#EXTINF)
                        lista_final.append(lineas[i+1]) # El link del video
        except:
            print(f"Error al conectar con la fuente: {url}")

    # GUARDAR EL ARCHIVO
    with open("lista_nicolas.m3u", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        # Usamos set() para no tener canales repetidos
        escritos = set()
        for i in range(0, len(lista_final), 2):
            nombre = lista_final[i]
            link = lista_final[i+1]
            if link not in escritos:
                f.write(f"{nombre}\n{link}\n")
                escritos.add(link)

    print(f"¡Listo! Se encontraron {len(escritos)} canales para el Nico.")

if __name__ == "__main__":
    ejecutar()
