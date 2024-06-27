# Napis funkciu append_text(filename, text), ktora doplni text `text` do suboru s nazvom `filename`.
# Ak je subor readonly, osetri tento pripad tak, ze vypises na vystup "Cannot write to file <filename>"
# Pre windows userov, ako nastavit, aby bol subor readonly:
# https://adamtheautomator.com/how-to-make-a-file-read-only/


def append_text(filename: str, text: str) -> None:
    try:
        with open(filename, 'a') as file:
            print(text, file=file)
    except PermissionError:
        print(f"Cannot write to file {filename}")


if __name__ == "__main__":
    append_text('normal_file.txt', 'Monty Python')
    append_text('readonly_file.txt', 'will not get there')
