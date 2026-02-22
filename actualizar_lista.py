import requests
import re

# Esta es la página que me diste
URL_FUENTE = "https://www.tvporinternet2.com/"

def buscar_links():
    canales_encontrados = []
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
        respuesta = requests.get(URL_FUENTE, headers=headers, timeout=15)
        
        if respuesta.status_code == 200:
            # Buscamos los links de video .m3u8
            links = re.findall(r'(https?://[^\s\'"]+\.m3u8[^\s\'"]*)', respuesta.text)
            
            for link in links:
                l = link.lower()
                if "tnt" in l or "espn" in l or "fox" in l:
                    nombre = "TNT SPORTS" if "tnt" in l else "ESPN"
                    canales_encontrados.append(f"#EXTINF:-1, {nombre}\n{link}")
    except:
        pass
    return canales_encontrados

def guardar_lista(canales):
    with open("lista_nicolas.m3u", "w") as f:
        f.write("#EXTM3U\n")
        for c in canales:
            f.write(c + "\n")

if __name__ == "__main__":
    datos = buscar_links()
    guardar_lista(datos)
