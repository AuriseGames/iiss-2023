import asyncio

async def descarga_archivo(url, nombre, tamanio):
    print(f"Descargando {url}...")
    await asyncio.sleep(size)  # Simulamos la descarga con una espera de 1 segundo por cada MB
    print(f"Archivo {filename} descargado")

async def main():
    archivos = [
        ("https://ejemplo.com/archivo1.txt", "archivo1.txt", 3),
        ("https://ejemplo.com/archivo2.txt", "archivo2.txt", 2),
        ("https://ejemplo.com/archivo3.txt", "archivo3.txt", 1)
    ]

    hilos = []
    for url, nombre, tamanio in archivos:
        hilo = asyncio.create_task(descarga_archivo(url, nombre, tamanio))
        hilos.append(hilo)

    await asyncio.gather(*hilos)

asyncio.run(main())