import os
import subprocess
import customtkinter as ctk
from pathlib import Path

app = ctk.CTk()
app.title("Mi Primera Ventana")
app.geometry("400x300")

folder_name = ctk.CTkEntry(app, width=200, placeholder_text="Nombre de carpeta")
folder_name.pack(pady=20)

folder_name.insert(0, "Descargas")

app.mainloop()

folder = Path.home() / folder_name.get()

#agregar los inputs para nombres de categorias

category_name = ctk.CTkEntry(app, width=200, placeholder_text="Nombre de categoria")
category_name.pack(pady=20)

category_name.insert(0, "Images")

category_name2 = ctk.CTkEntry(app, width=200, placeholder_text="Nombre de categoria")
category_name2.pack(pady=20)

category_name2.insert(0, "Documents")

category_name3 = ctk.CTkEntry(app, width=200, placeholder_text="Nombre de categoria")
category_name3.pack(pady=20)

category_name3.insert(0, "Videos")

category_name4 = ctk.CTkEntry(app, width=200, placeholder_text="Nombre de categoria")
category_name4.pack(pady=20)

category_name4.insert(0, "Music")

category_name5 = ctk.CTkEntry(app, width=200, placeholder_text="Nombre de categoria")
category_name5.pack(pady=20)

category_name5.insert(0, "Others")

categories = {

    category_name2.get(): [".pdf", ".docx", ".txt", ".xlsx"],

    category_name3.get(): [".pdf", ".docx", ".txt", ".xlsx"],

    category_name4.get(): [".mp4", ".avi", ".mkv"],

    category_name5.get(): [".mp3", ".wav"],

}

others = ["Others"]

extension_category = {}

for category, exts in categories.items():

    for ext in exts:

        extension_category[ext.lower()] = category

def organizer():

    files = [f for f in folder.iterdir() if f.is_file()]

    for file in files:

        if file.name != "organizar.py":
            ext = file.suffix.lower()

    category = extension_category.get(ext, "Others")

    dir = folder / category

    dir.mkdir(exist_ok=True)

    file.rename(dir / file.name)
    subprocess.run(['notify-send', 'Done!', f"Movido {file.name} a {category}/"])
