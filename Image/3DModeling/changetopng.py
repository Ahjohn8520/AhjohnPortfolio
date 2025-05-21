import os
from PIL import Image

def convert_and_rename_images(folder_path):
    image_exts = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff')
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(image_exts)]
    files.sort()

    for idx, filename in enumerate(files, start=1):
        src = os.path.join(folder_path, filename)
        new_name = f"{idx:02d}.png"
        dst = os.path.join(folder_path, new_name)

        with Image.open(src) as img:
            img.convert("RGBA").save(dst, "PNG")
        if src != dst:
            os.remove(src)
        print(f"Converted and renamed: {filename} -> {new_name}")

if __name__ == "__main__":
    folder = os.path.dirname(os.path.abspath(__file__))
    convert_and_rename_images(folder)