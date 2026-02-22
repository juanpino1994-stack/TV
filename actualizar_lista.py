import requests
import re

URL_STREAM = "https://deportes.ksdjugfsddeports.com/stream.php?canal=tntsportsar&target=2"

def ejecutar():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Referer': 'https://embed.ksdjugfsddeports.com/'
    }
    
    try:
        response = requests.get(URL_STREAM, headers=headers, timeout=15)
        # Buscamos el link .m3u8
        match = re.search(r'["\'](https?://[^\s\'"]+\.m3u8[^\s\'"]*)["\']', response.text)
        
        # Forzamos que el archivo se escriba en formato estándar de texto
        with open("lista_nicolas.m3u", "w", encoding="utf-8", newline='\n') as f:
            f.write("#EXTM3U\n")
            if match:
                link_raw = match.group(1).replace('\\/', '/')
                # El formato exacto: #EXTINF, luego nombre, luego link en linea nueva
                f.write("#EXTINF:-1, TNT SPORTS\n")
                f.write(f"{link_raw}|User-Agent=Mozilla/5.0&Referer=https://embed.ksdjugfsddeports.com/\n")
                print("Canal escrito correctamente.")
            else:
                # Si no hay link, ponemos uno de error para que la app al menos lea ALGO
                f.write("#EXTINF:-1, ERROR - CANAL NO ENCONTRADO\n")
                f.write("http://error.com/video.m3u8\n")
                print("No se encontró link.")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ejecutar()
