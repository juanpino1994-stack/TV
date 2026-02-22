import requests

# Esta fuente es mucho mejor para nosotros (Chile, Argentina, Premium Latam)
URL_MAESTRA = "https://raw.githubusercontent.com/m3u4u/m3u4u/main/latino.m3u"

def ejecutar():
    print("Buscando canales latinos...")
    try:
        # Usamos un User-Agent de Smart TV para que los links no se mueran
        headers = {'User-Agent': 'Mozilla/5.0 (SmartHub; SMART-TV; Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0'}
        respuesta = requests.get(URL_MAESTRA, headers=headers, timeout=30)
        
        if respuesta.status_code == 200:
            # Filtramos para que no pesque canales raros
            lineas = respuesta.text.split('\n')
            lista_limpia = []
            
            for i in range(len(lineas)):
                # Si la línea tiene info del canal, revisamos que sea de interés
                if lineas[i].startswith("#EXTINF"):
                    nombre = lineas[i].upper()
                    # Si quieres filtrar por países, puedes agregar condiciones aquí
                    if i + 1 < len(lineas):
                        lista_limpia.append(lineas[i])
                        lista_limpia.append(lineas[i+1])
            
            with open("lista_nicolas.m3u", "w", encoding="utf-8") as f:
                f.write("#EXTM3U\n")
                f.write("\n".join(lista_limpia))
            
            print(f"¡Listo! Se cargaron {len(lista_limpia)//2} canales latinos.")
        else:
            print("La fuente falló. Intentando con fuente de respaldo...")
            # Aquí podrías poner otra URL si la primera falla
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ejecutar()
