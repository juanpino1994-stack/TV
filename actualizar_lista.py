import requests
import re

# La fuente donde está el video
URL_FUENTE = "https://deportes.ksdjugfsddeports.com/stream.php?canal=tntsportsar&target=2"

def ejecutar():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Referer': 'https://embed.ksdjugfsddeports.com/'
    }
    
    try:
        r = requests.get(URL_FUENTE, headers=headers, timeout=15)
        
        # CAMBIO CLAVE: Ahora buscamos SOLAMENTE links que terminen en .m3u8
        # Ignoramos cualquier cosa que termine en .com
        links = re.findall(r'["\'](https?://[^\s\'"]+\.m3u8[^\s\'"]*)["\']', r.text)
        
        with open("lista_nicolas.m3u", "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            
            if links:
                # Limpiamos el link encontrado
                link_final = links[0].replace('\\/', '/')
                f.write("#EXTINF:-1, TNT SPORTS\n")
                f.write(f"{link_final}|User-Agent=Mozilla/5.0&Referer=https://embed.ksdjugfsddeports.com/\n")
                print(f"¡Éxito! Se encontró un archivo de video real: {link_final}")
            else:
                f.write("#EXTINF:-1, ERROR: No se encontro archivo .m3u8\n")
                f.write("http://error.com/revisar_fuente.m3u8\n")
                print("No se encontró ningún link de video .m3u8, solo links .com")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ejecutar()
