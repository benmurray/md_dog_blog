import pathlib
import markdown


INPUT_DIR = pathlib.Path().resolve().parent / 'test_input'
OUTPUT_DIR = pathlib.Path().resolve().parent / 'test_output'


def main():
    if not OUTPUT_DIR.exists():
        OUTPUT_DIR.mkdir(exist_ok=True)

    for path_object in INPUT_DIR.rglob('*'):
        if path_object.is_file():
            year = path_object.parts[-4]
            month = path_object.parts[-3]
            day = path_object.parts[-2]
            title = path_object.name
            with open(path_object, "r", encoding="utf-8") as input_file:
                raw_text = input_file.read()
            html = markdown.markdown(raw_text)

            output_path = OUTPUT_DIR / year / month / day
            output_path.mkdir(parents=True, exist_ok=True)
            full_filename = output_path / path_object.stem
            full_filename = output_path / (full_filename.stem + '.html')

            # convert to html and write file
            with open(full_filename, 'w', encoding='utf-8', errors="xmlcharrefreplace") as output_file:
                output_file.write(html)


if __name__ == '__main__':
    main()
