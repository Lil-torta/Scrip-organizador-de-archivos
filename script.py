from pathlib import Path
import shutil

SIMULAR = False   # cámbialo a False cuando todo se vea bien

CATEGORIAS = {
    '.pdf': 'Documentos',
    '.docx': 'Documentos',
    '.jpg': 'Imagenes',
    '.png': 'Imagenes',
}


def manejar_duplicados(destino: Path) -> Path:
    if not destino.exists():
        return destino

    contador = 1
    while True:
        nueva = destino.with_name(f'{destino.stem}_{contador}{destino.suffix}')
        if not nueva.exists():
            return nueva
        contador += 1


def organizar(carpeta: Path) -> None:
    for archivo in carpeta.iterdir():
        if not archivo.is_file():
            continue

        categoria = CATEGORIAS.get(archivo.suffix.lower(), 'Otros')
        carpeta_destino = carpeta / categoria
        destino = manejar_duplicados(carpeta_destino / archivo.name)

        print(f'{archivo.name} -> {categoria}/{destino.name}')

        if not SIMULAR:
            carpeta_destino.mkdir(exist_ok=True)
            shutil.move(archivo, destino)


if __name__ == '__main__':
    organizar(Path.home() / 'Downloads')