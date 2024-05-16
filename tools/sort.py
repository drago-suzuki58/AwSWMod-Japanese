import os
import re

# tsvファイルの行を番号順にソートするプログラム

def sort_lines(directory, filename):
    with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
        lines = file.readlines()

    lines_with_numbers = []
    for line in lines:
        match = re.search(r':(\d+):', line)
        if match:
            line_number = str(match.group(1)).zfill(4)
            lines_with_numbers.append((line_number, line))

    lines_with_numbers.sort()

    output_filename = f"output_{filename}"
    with open(os.path.join(directory, output_filename), 'w', encoding='utf-8') as file:
        for _, line in lines_with_numbers:
            file.write(line)
    return output_filename

if __name__ == '__main__':
    # ディレクトリの指定
    directory = ''

    for filename in os.listdir(directory):
        if filename.startswith('translated_output_') and filename.endswith('.tsv'):
            sort_lines(directory, filename)