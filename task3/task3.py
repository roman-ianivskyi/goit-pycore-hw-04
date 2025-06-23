
from colorama import Fore
import sys
from pathlib import Path

identation_symbol = "    "

def print_dir(directory: Path, identation: str = ""):
    

    for path in directory.iterdir():
        if path.is_dir():
            print(identation + f"{Fore.GREEN}{path.name}/")
            print_dir(path, identation + identation_symbol)
        else:
            print(identation + f"{Fore.BLUE}{path.name}")


def main():
    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
        if path.exists():
            if path.is_dir():
                print_dir(path)
            else:
                print(f"Entered path {path} is not a directory")
        else:
            print(f"Entered path {path} does not exist")
    else:
        print("Please enter directory path as an argument, for example task3.py /home/user")


if __name__ == "__main__":
    main()