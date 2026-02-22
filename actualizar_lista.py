import requests
import re

# Dirección de la fuente
URL_FUENTE = "https://deportes.ksdjugfsddeports.com/stream.php?canal=tntsportsar&target=2"

def ejecutar():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Referer': 'https://embed.ksdjugfsddeports.com/'
    }
    
    try:
        # 1. Obtenemos la página
        r = requests.get(URL_FUENTE, headers=headers, timeout=15)
        
        # 2. Buscamos el link del video (.m3u8)
        # Este buscador es más flexible para encontrar el link
        links = re.findall(r'(https?://[^\s\'"]+\.m3u8[^\s\'"]*)', r.text)
        
        # 3. Escribimos el archivo de forma ultra-limpia
        with open("lista_nicolas.m3u", "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n") # Encabezado obligatorio
            
            if links:
                # Limpiamos el primer link encontrado
                link_final = links[0].replace('\\/', '/').split('"')[0].split("'")[0]
                
                # Formato M3U puro: Nombre del canal y luego el Link
                f.write("#EXTINF:-1, TNT SPORTS\n")
                f.write(f"{link_final}|User-Agent=Mozilla/5.0&Referer=https://embed.ksdjugfsddeports.com/\n")
                print(f"Canal encontrado y guardado.")
            else:
                # Si no hay canal, ponemos uno de prueba para ver si la app lee el archivo
                f.write("#EXTINF:-1, CANAL DE PRUEBA (ARCHIVO LEIDO)\n")
                f.write("http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4\n")
                print("No se encontró canal, se puso uno de prueba.")
                
    except Exception as e:
        print(f"Error técnico: {e}")

if __name__ == "__main__":
    ejecutar()
