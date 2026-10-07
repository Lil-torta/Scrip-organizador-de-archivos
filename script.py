from pathlib import Path
import shutil

mapeo = {
    '.pdf': 'PDFs',
    '.docx': 'Documentos',
    '.jpeg': 'Imagenes',
    '.png': 'Imagenes',

}

descargas = Path.home() / 'Downloads'
for archivo in descargas.iterdir():
    #print(archivo.name, archivo.suffix)

    if not archivo.is_file():
        continue

    categorias = mapeo.get(archivo.suffix.lower())

    if categorias:
        destino = descargas / categorias
        destino.mkdir(exist_ok=True)

        shutil.move(archivo, destino / archivo.name ) 
    print(mapeo.get('*.jpg'))
