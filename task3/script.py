import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)


def display_tree(path: Path, indent: str = ""):
    directories = []
    files = []

    for item in path.iterdir():
        if item.is_dir():
            directories.append(item)
        elif item.is_file():
            files.append(item)

    directories.sort()
    files.sort()

    for directory in directories:
        print(f"{indent}📂 {Fore.BLUE}{directory.name}")
        display_tree(directory, indent + "    ")


    for file in files:
        print(f"{indent}📜 {Fore.GREEN}{file.name}")


def main():
    if len(sys.argv) < 2:
        print(Fore.RED + "Помилка: вкажіть шлях до директорії.")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(Fore.RED + f"Помилка: шлях '{dir_path}' не існує.")
        sys.exit(1)

    if not dir_path.is_dir():
        print(Fore.RED + f"Помилка: об'єкт '{dir_path}' не є директорією.")
        sys.exit(1)

    print(f"📦 {Fore.CYAN}{dir_path.name}")
    display_tree(dir_path, "  ")


if __name__ == "__main__":
    main()