import os

def rename_images_in_folder(folder_path):
    # Supported image extensions
    image_exts = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff')
    files = [f for f in os.listdir(folder_path) if f.lower().endswith(image_exts)]
    files.sort()  # Sort files alphabetically

    # First, rename all files to temporary names to avoid name conflicts
    temp_names = []
    for idx, filename in enumerate(files):
        ext = os.path.splitext(filename)[1]
        temp_name = f"temp_rename_{idx}{ext}"
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, temp_name)
        os.rename(src, dst)
        temp_names.append(temp_name)

    # Then, rename from temporary names to final names
    for idx, temp_name in enumerate(temp_names, start=1):
        ext = os.path.splitext(temp_name)[1]
        new_name = f"{idx:02d}{ext}"
        src = os.path.join(folder_path, temp_name)
        dst = os.path.join(folder_path, new_name)
        os.rename(src, dst)
        print(f"Renamed: {temp_name} -> {new_name}")

if __name__ == "__main__":
    folder = os.path.dirname(os.path.abspath(__file__))
    rename_images_in_folder(folder)