from datetime import datetime
from functools import cache
from pathlib import Path
from sys import argv
from typing import Iterable


def main() -> None:
    if (count := len(files())) > 0:
        for i, path in enumerate(files(), 1):
            print(f"{i}. {path}")

        if count > 1:
            question = f"Do you really want to rename all {count} files?"
        else:
            question = "Do you really want to rename that file?"

        if ask(question):
            for path in files():
                rename(path)
    else:
        print("No files have been found")


def ask(question: str) -> bool:
    while True:
        try:
            answer = input(f"{question} [y/n] ").lower()
            if answer == "y":
                return True
            if answer == "n":
                return False
            print('Please, type either "y" for yes or "n" for no')
        finally:
            print()


@cache
def files() -> list[Path]:
    def files_() -> Iterable[Path]:
        for path in Path.cwd().rglob("*"):
            if path.is_file() and path != Path(argv[0]):
                yield path

    return sorted(files_())


def rename(path: Path) -> None:
    creation_datetime = datetime.fromtimestamp(path.stat().st_ctime)
    filename = f"{format(creation_datetime, '%Y%m%d %H%M')}{path.suffix}"
    new_path = path.parent / filename
    if new_path.exists():
        print(f"OLD: {path}\n(!) Skipping to avoid overwriting another file\n")
    else:
        path.rename(new_path)
        print(f"OLD: {path}\nNEW: {new_path}\n")


if __name__ == "__main__":
    main()
