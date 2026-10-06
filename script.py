from pathlib import Path
import shutil

carpeta = Path.home() / 'Downloads'
for archivo in carpeta.iterdir():
    print(archivo.name, archivo.suffix)

categorias = {
    '.pdf': 'Documentos',
    '.docx': 'Documentos',
    '.jpeg': 'Imagenes',
    '.png': 'Imagenes'

}

pdf = Path.home() / 'Downloads' / 'pdf'
pdf.mkdir(exist_ok=True)

for archivo in Path('.').glob('*.pdf'):
    shutil.move(
        archivo,
        pdf / archivo.name
    )