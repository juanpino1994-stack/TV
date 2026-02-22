import requests

# FUENTES INTERNACIONALES (Muy estables)
FUENTES = [
    "https://iptv-org.github.io/iptv/index.m3u", # La fuente más grande del mundo
    "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/cl.m3u", # Canales de Chile
    "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/ar.m3u"  # Canales de Argentina
]

def ejecutar():
    print("Iniciando recolección de emergencia...")
    canales_totales = 0
    links_vistos = set()

    try:
        with open("lista_nicolas.m3u", "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            
            for url in FUENTES:
                print(f"Probando fuente: {url}")
                try:
                    r = requests.get(url, timeout=30)
                    r.raise_for_status() # Si la página da error, salta a la siguiente
                    
                    lineas = r.text.split('\n')
                    for i in range(len(lineas)):
                        if lineas[i].startswith("#EXTINF"):
                            if i + 1 < len(lineas):
                                link = lineas[i+1].strip()
                                if link.startswith("http") and link not in links_vistos:
                                    f.write(f"{lineas[i]}\n{link}\n")
                                    links_vistos.add(link)
                                    canales_totales += 1
                except Exception as e:
                    print(f"Fallo en esta fuente: {e}")

            if canales_totales == 0:
                f.write("#EXTINF:-1, ERROR: No se pudieron recolectar canales\n")
                f.write("http://error.com/sin_canales.m3u8\n")
                
        print(f"Finalizado. Se encontraron {canales_totales} canales.")

    except Exception as e:
        print(f"Error crítico al crear el archivo: {e}")

if __name__ == "__main__":
    ejecutar()
