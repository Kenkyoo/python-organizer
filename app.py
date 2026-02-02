import os

from pathlib import Path

folder = Path.home() / "Descargas"

categories = {

    "Images": [".png", ".jpg", ".jpeg", ".gif"],

    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],

    "Videos": [".mp4", ".avi", ".mkv"],

    "Music": [".mp3", ".wav"],

}

others = ["Others"]

extension_category = {}

for category, exts in categories.items():

    for ext in exts:

        extension_category[ext.lower()] = category

files = [f for f in folder.iterdir() if f.is_file()]

for file in files:

    if file.name != "organizar.py":
        ext = file.suffix.lower()

    category = extension_category.get(ext, "Others")

    dir = folder / category

    dir.mkdir(exist_ok=True)

    file.rename(dir / file.name)

    print(f"Movido {file.name} a {category}/")
