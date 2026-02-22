import requests

# Esta es la "Lista Maestra" que siempre funciona
URL_MAESTRA = "https://raw.githubusercontent.com/GuuS-it/IPTV-Latino/master/Lista.m3u"

def ejecutar():
    print("Iniciando clonación de la lista maestra...")
    try:
        # El robot descarga la lista completa de una
        respuesta = requests.get(URL_MAESTRA, timeout=30)
        
        # Si la descarga fue exitosa (Código 200)
        if respuesta.status_code == 200:
            content = respuesta.text
            
            # Guardamos exactamente lo mismo en tu archivo
            with open("lista_nicolas.m3u", "w", encoding="utf-8") as f:
                f.write(content)
            
            print("¡Clonación exitosa! El Nico ya tiene todos los canales.")
        else:
            print(f"Error: La lista maestra no respondió (Código {respuesta.status_code})")
            
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    ejecutar()
