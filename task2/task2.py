from pathlib import Path

def get_cats_info(path: str | Path) -> list[dict[str, str | int]]:
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                try:
                    id, name, age = line.split(",", 2)
                    cats.append({ 
                        "id": id.strip(),
                        "name": name.strip(),
                        "age": int(age.strip())
                    })
                except ValueError:
                    continue
    except FileNotFoundError:  
        print(f"File {path.absolute()} not found.")
        return []
    return cats

print(get_cats_info(Path("/Users/tetyanaburii/Desktop/python_homeworks/homework6/cats.txt")))