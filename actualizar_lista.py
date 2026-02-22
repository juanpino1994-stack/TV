import requests
import re

# Canal específico de prueba
URL_STREAM = "https://deportes.ksdjugfsddeports.com/stream.php?canal=tntsportsar&target=2"

def ejecutar():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        'Referer': 'https://embed.ksdjugfsddeports.com/'
    }
    
    try:
        # 1. El robot intenta entrar a la señal
        response = requests.get(URL_STREAM, headers=headers, timeout=15)
        
        # 2. Busca el link .m3u8 entre las comillas
        match = re.search(r'["\'](https?://[^\s\'"]+\.m3u8[^\s\'"]*)["\']', response.text)
        
        with open("lista_nicolas.m3u", "w") as f:
            f.write("#EXTM3U\n")
            if match:
                link_raw = match.group(1).replace('\\/', '/')
                # 3. Agregamos el "disfraz" al final del link para saltar el bloqueo
                link_con_disfraz = f"{link_raw}|User-Agent=Mozilla/5.0&Referer=https://embed.ksdjugfsddeports.com/"
                f.write(f"#EXTINF:-1, TNT SPORTS\n{link_con_disfraz}\n")
                print("¡Éxito! Link generado con disfraz.")
            else:
                f.write("#EXTINF:-1, Canal no encontrado en el codigo\nhttp://error.com\n")
                print("No se encontró el link m3u8.")
                
    except Exception as e:
        print(f"Error al conectar: {e}")

if __name__ == "__main__":
    ejecutar()
