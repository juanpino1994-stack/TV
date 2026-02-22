import requests
import re

# --- LISTA DE CANALES DESDE TUS CAPTURAS ---
CANALES = [
    {
        "nombre": "TNT SPORTS", 
        "url": "https://deportes.ksdjugfsddeports.com/stream.php?canal=tntsportsar&target=2"
    },
    {
        "nombre": "TUDN", 
        "url": "https://deportes.ksdjugfsddeports.com/stream.php?canal=tudn&target=1"
    },
    {
        "nombre": "ESPN PREMIUM", 
        "url": "https://deportes.ksdjugfsddeports.com/stream.php?canal=espnpremium&target=1"
    }
]

def obtener_m3u8(url_fuente):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Referer': 'https://ksdjugfsddeports.com/'
    }
    try:
        # Paso 1: Entrar a la página del canal
        r1 = requests.get(url_fuente, headers=headers, timeout=10)
        
        # Paso 2: Buscar el iframe (lo que sale en tus capturas)
        embed_match = re.search(r'https?://embed\.ksdjugfsddeports\.com/embed2/[^"\']+\.html', r1.text)
        
        if embed_match:
            url_embed = embed_match.group(0)
            headers['Referer'] = url_fuente
            
            # Paso 3: Entrar al reproductor y buscar el link .m3u8
            r2 = requests.get(url_embed, headers=headers, timeout=10)
            video_match = re.search(r'["\'](https?://[^\s\'"]+\.m3u8[^\s\'"]*)["\']', r2.text)
            
            if video_match:
                return video_match.group(1).replace('\\/', '/')
    except:
        pass
    return None

def ejecutar():
    print(f"Actualizando {len(CANALES)} canales...")
    
    with open("lista_nicolas.m3u", "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        
        for canal in CANALES:
            print(f"Procesando: {canal['nombre']}...")
            link = obtener_m3u8(canal['url'])
            
            if link:
                f.write(f"#EXTINF:-1, {canal['nombre']}\n")
                # El "disfraz" para que el Nico no vea el error 403
                f.write(f"{link}|User-Agent=Mozilla/5.0&Referer=https://embed.ksdjugfsddeports.com/&Origin=https://embed.ksdjugfsddeports.com\n")
                print(" -> Link encontrado.")
            else:
                print(" -> No se pudo extraer el video.")

if __name__ == "__main__":
    ejecutar()
