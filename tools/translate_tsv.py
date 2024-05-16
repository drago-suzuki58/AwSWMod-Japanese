import os
import re
from googletrans import Translator

# tsvファイルのセリフのみ抽出して翻訳するプログラム
# src: 翻訳元言語 dest: 翻訳先言語 で指定できる

def translate_lines(directory, filename, src='en', dest='ja'):
    translator = Translator()

    with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
        lines = file.readlines()

    translated_lines = []
    for line in lines:
        parts = line.split('\t')
        text = parts[4].strip()

        match = re.match(r'^(.*)"(.*)"$', text)
        if match:
            text_to_translate = match.group(2)

            result = translator.translate(text_to_translate, src=src, dest=dest)
            translated_text = result.text

            parts[4] = f'{match.group(1)}"{translated_text}"'
            print(f'{match.group(1)}"{translated_text}"') # progress check

        translated_line = '\t'.join(parts)
        translated_lines.append(translated_line + '\n')
    output_filename = f"translated_{filename}"
    with open(os.path.join(directory, output_filename), 'w', encoding='utf-8') as file:
        for line in translated_lines:
            file.write(line)
    return output_filename

if __name__ == '__main__':
    # ディレクトリの指定
    directory = ''

    files = os.listdir(directory)
    for filename in files:
        if filename.endswith('.tsv'):
            translate_lines(directory, filename)