import os
import subprocess
import customtkinter as ctk
from pathlib import Path

# Configuración de tema
ctk.set_appearance_mode("dark")  # "dark" o "light"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

app = ctk.CTk()
app.title("File Organizer")
app.geometry("500x650")

# Título
titulo = ctk.CTkLabel(app, text="📁 Organizador de Archivos", font=("Arial", 24, "bold"))
titulo.pack(pady=20)

# Frame para carpeta principal
frame_folder = ctk.CTkFrame(app)
frame_folder.pack(pady=10, padx=20, fill="x")

label_folder = ctk.CTkLabel(frame_folder, text="Carpeta a organizar:", font=("Arial", 14))
label_folder.pack(pady=5)

folder_name = ctk.CTkEntry(frame_folder, width=300, placeholder_text="Nombre de carpeta")
folder_name.pack(pady=5)
folder_name.insert(0, "Descargas")

# Frame para categorías
frame_categories = ctk.CTkFrame(app)
frame_categories.pack(pady=10, padx=20, fill="both", expand=True)

label_categories = ctk.CTkLabel(frame_categories, text="Categorías:", font=("Arial", 14))
label_categories.pack(pady=10)

# Inputs de categorías con labels
categorias = [
    ("🖼️ Imágenes:", "Images"),
    ("📄 Documentos:", "Documents"),
    ("🎬 Videos:", "Videos"),
    ("🎵 Música:", "Music"),
    ("📦 Otros:", "Others")
]

inputs = {}
for emoji_label, default_value in categorias:
    mini_frame = ctk.CTkFrame(frame_categories, fg_color="transparent")
    mini_frame.pack(pady=3)

    label = ctk.CTkLabel(mini_frame, text=emoji_label, width=120, anchor="w")
    label.pack(side="left", padx=5)

    entrada = ctk.CTkEntry(mini_frame, width=200)
    entrada.pack(side="left", padx=5)
    entrada.insert(0, default_value)

    inputs[default_value] = entrada

def organizer():
    folder = Path.home() / folder_name.get()

    categories = {
        inputs["Images"].get(): [".jpg", ".png", ".gif", ".jpeg", ".svg"],
        inputs["Documents"].get(): [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
        inputs["Videos"].get(): [".mp4", ".avi", ".mkv", ".mov"],
        inputs["Music"].get(): [".mp3", ".wav", ".flac"],
    }

    extension_category = {}
    for category, exts in categories.items():
        for ext in exts:
            extension_category[ext.lower()] = category

    files = [f for f in folder.iterdir() if f.is_file()]
    count = 0
    for file in files:
        if file.name != "organizar.py":
            ext = file.suffix.lower()
            category = extension_category.get(ext, inputs["Others"].get())
            dir = folder / category
            dir.mkdir(exist_ok=True)
            file.rename(dir / file.name)
            count += 1

    subprocess.run(['notify-send', '✅ Completado!', f"Se organizaron {count} archivos"])
    status_label.configure(text=f"✅ {count} archivos organizados", text_color="green")

# Botón de organizar
boton = ctk.CTkButton(app, text="🚀 Organizar Archivos", command=organizer,
                      height=40, font=("Arial", 16, "bold"))
boton.pack(pady=20)

# Label de estado
status_label = ctk.CTkLabel(app, text="", font=("Arial", 12))
status_label.pack(pady=5)

app.mainloop()
