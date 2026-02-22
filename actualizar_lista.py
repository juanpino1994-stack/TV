import requests
import re
import time

URL_PRINCIPAL = "https://embed.ksdjugfsddeports.com/"

def buscar_links():
    canales_finales = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'Referer': URL_PRINCIPAL
    }

    try:
        print("Entrando a la vitrina de canales...")
        r = requests.get(URL_PRINCIPAL, headers=headers, timeout=20)
        # 1. Buscamos todos los archivos .php (que son los canales: tudn.php, tntsports.php, etc.)
        paginas_canales = re.findall(r'href=["\'](https?://embed\.ksdjugfsddeports\.com/[^"\']+\.php)["\']', r.text)
        
        # Eliminamos duplicados y limitamos a los primeros para no saturar (puedes aumentar el número)
        paginas_canales = list(set(paginas_canales))[:15] 

        for url_canal in paginas_canales:
            try:
                nombre_canal = url_canal.split('/')[-1].replace('.php', '').upper()
                print(f"Buscando señal en: {nombre_canal}")
                
                # 2. Entramos a cada página de canal
                r_canal = requests.get(url_canal, headers=headers, timeout=10)
                
                # 3. Buscamos el link del video (.m3u8) dentro del código de esa página
                links_video = re.findall(r'["\'](https?://[^\s\'"]+\.m3u8[^\s\'Raw"]*)["\']', r_canal.text)
                
                if links_video:
                    link_final = links_video[0].replace('\\/', '/')
                    canales_finales.append(f"#EXTINF:-1, {nombre_canal}\n{link_final}")
                    print(f"✅ ¡Encontrado!")
                
                time.sleep(1) # Pausa breve para no ser bloqueados
            except:
                continue
                
    except Exception as e:
        print(f"Error general: {e}")
        
    return canales_finales

def guardar_lista(canales):
    with open("lista_nicolas.m3u", "w") as f:
        f.write("#EXTM3U\n")
        if canales:
            for c in canales:
                f.write(c + "\n")
        else:
            f.write("#EXTINF:-1, El robot esta escaneando los canales, vuelve en unos minutos\nhttp://espera.com\n")

if __name__ == "__main__":
    datos = buscar_links()
    guardar_lista(datos)
