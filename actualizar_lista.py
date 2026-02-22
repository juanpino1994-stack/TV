import requests
import re

# La página que me pasaste
URL_INICIAL = "https://deportes.ksdjugfsddeports.com/stream.php?canal=tntsportsar&target=2"

def buscar_en_profundidad():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Referer': 'https://embed.ksdjugfsddeports.com/'
    }
    
    try:
        # El robot entra directamente al stream.php
        r = requests.get(URL_INICIAL, headers=headers, timeout=20)
        
        # Busca el link del video .m3u8
        links = re.findall(r'["\'](https?://[^\s\'"]+\.m3u8[^\s\'"]*)["\']', r.text)
        
        with open("lista_nicolas.m3u", "w") as f:
            f.write("#EXTM3U\n")
            if links:
                # Limpia el link (quita barras raras)
                link_final = links[0].replace('\\/', '/')
                f.write(f"#EXTINF:-1, TNT SPORTS\n{link_final}\n")
                print("¡Link encontrado con éxito!")
            else:
                f.write("#EXTINF:-1, Canal no disponible ahora\nhttp://vacio.com\n")
                print("No se encontró el .m3u8 en el stream")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    buscar_en_profundidad()
