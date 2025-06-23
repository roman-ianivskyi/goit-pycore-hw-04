
def get_cats_info(path: str):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats = []
            while True:
                line = file.readline()

                if not line:
                    break

                splitted_line = line.strip().split(',')

                if len(splitted_line) != 3:
                    raise ValueError(f'Line "{line}" in file {path} is malformed, expected format is id,name,age')

                cats.append(
                    {
                        'id': splitted_line[0],
                        'name': splitted_line[1],
                        'age': splitted_line[2]
                    }
                )

            return cats
        
    except Exception as e:
        print(f"Error reading file {path}: {e}")
        return None, None

print(get_cats_info("task2/cats_file.txt"))
print(get_cats_info("task2/cats_file_malformed.txt"))