import requests

# Fuentes masivas con miles de canales (Latino, España, Premium)
FUENTES = [
    "https://raw.githubusercontent.com/GuuS-it/IPTV-Latino/master/Lista.m3u",
    "https://raw.githubusercontent.com/marcofbb/iptv/master/latam.m3u",
    "https://raw.githubusercontent.com/Kuevitas/Kuevitas.github.io/master/lista.m3u"
]

def ejecutar():
    print("Iniciando recolección masiva de canales...")
    canales_totales = 0
    
    # Usamos un set para no repetir links si están en varias fuentes
    links_vistos = set()

    with open("lista_nicolas.m3u", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        
        for url in FUENTES:
            try:
                print(f"Descargando fuente: {url}")
                r = requests.get(url, timeout=20)
                lineas = r.text.split('\n')
                
                for i in range(len(lineas)):
                    # Si la línea tiene la info del canal
                    if lineas[i].startswith("#EXTINF"):
                        if i + 1 < len(lineas):
                            link = lineas[i+1].strip()
                            # Si es un link y no lo hemos agregado antes
                            if link.startswith("http") and link not in links_vistos:
                                f.write(f"{lineas[i]}\n{link}\n")
                                links_vistos.add(link)
                                canales_totales += 1
            except Exception as e:
                print(f"No se pudo leer la fuente {url}: {e}")

    print(f"¡Terminado! El Nico ahora tiene {canales_totales} canales en su lista.")

if __name__ == "__main__":
    ejecutar()
