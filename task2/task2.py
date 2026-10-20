from pathlib import Path

def get_cats_info(path):
    file_path = Path(path)
    cats_info = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:

            for line in file:
                cleaned_line = line.strip()
                if not cleaned_line:
                    continue
                try:
                    cat_id, name,  age = cleaned_line.split(",")
                    cat_data = {"id": cat_id, "name": name, "age": age}
                    cats_info.append(cat_data)
                except ValueError:
                    print(f"Pass: {cleaned_line}")
                    continue


    except FileNotFoundError:
        print(f"File {file_path} not found")
        return []
    except Exception as e:
        print(f"Error while reading a file: {e}")
        return []

    return cats_info


cats_info = get_cats_info("cats_file.txt")
print(cats_info)
# [
#     {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
#     {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
#     {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
#     {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
#     {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
# ]
