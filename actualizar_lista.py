import requests
import re

# Esta es la página que elegiste, no la vamos a cambiar
URL_FUENTE = "https://www.tvporinternet2.com/"

def buscar_links():
    canales_encontrados = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://www.google.com/'
    }
    
    try:
        # El robot ahora entra con "disfraz" de navegador Chrome
        sesion = requests.Session()
        respuesta = sesion.get(URL_FUENTE, headers=headers, timeout=20)
        
        if respuesta.status_code == 200:
            # Buscamos links que tengan .m3u8, incluso si están escondidos en el código
            links = re.findall(r'(https?://[^\s\'"]+\.m3u8[^\s\'"]*)', respuesta.text)
            
            # Si encuentra links, los limpia y les da formato
            for i, link in enumerate(list(set(links))):
                link_limpio = link.replace('\\', '')
                canales_encontrados.append(f"#EXTINF:-1, Canal {i+1}\n{link_limpio}")
    except Exception as e:
        print(f"Error: {e}")
        
    return canales_encontrados

def guardar_lista(canales):
    with open("lista_nicolas.m3u", "w") as f:
        f.write("#EXTM3U\n")
        if canales:
            for c in canales:
                f.write(c + "\n")
        else:
            # Si falla, nos avisará en el archivo
            f.write("#EXTINF:-1, El robot no encontro links aun\nhttp://link_vacio.com\n")

if __name__ == "__main__":
    datos = buscar_links()
    guardar_lista(datos)
