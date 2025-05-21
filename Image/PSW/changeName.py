import os

def rename_images_in_folder(folder_path):
    # Supported image extensions
    image_exts = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff')
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(image_exts)]
    files.sort()  # Sort files alphabetically

    for idx, filename in enumerate(files, start=1):
        ext = os.path.splitext(filename)[1]
        new_name = f"{idx:02d}{ext}"
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)
        os.rename(src, dst)
        print(f"Renamed: {filename} -> {new_name}")

if __name__ == "__main__":
    folder = os.path.dirname(os.path.abspath(__file__))
    rename_images_in_folder(folder)