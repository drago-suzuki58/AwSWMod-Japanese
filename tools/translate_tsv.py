import os
import re
import binascii
from googletrans import Translator

# tsvファイルのセリフのみ抽出して翻訳するプログラム
# src: 翻訳元言語 dest: 翻訳先言語 で指定できる

def base16_encode(s):
    try:
        return binascii.hexlify(s.encode()).decode()
    except Exception:
        return s

def base16_decode(s):
    try:
        return binascii.unhexlify(s.encode()).decode()
    except Exception:
        return s

def translate_lines(directory, filename, src='en', dest='ja'):
    translator = Translator()

    with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
        lines = file.readlines()

    translated_lines = []
    for line in lines:
        parts = line.split('\t')
        text = parts[4].strip()

        match_str = re.match(r'^(.*)"(.*)"$', text)
        if match_str:
            text_to_translate = match_str.group(2)

            # Base16エンコードされるべき部分を探し、存在する場合はエンコードする
            matches = re.findall(r'\[.*?\]', text_to_translate)
            if matches:
                for match in matches:
                    encoded_match = base16_encode(match[1:-1])
                    text_to_translate = text_to_translate.replace(match, '[' + encoded_match + ']')
                    print(f'{match} -> {encoded_match}') # progress check

            matches = re.findall(r'\{.*?\}', text_to_translate)
            if matches:
                for match in matches:
                    encoded_match = base16_encode(match[1:-1])
                    text_to_translate = text_to_translate.replace(match, '{' + encoded_match + '}')
                    print(f'{match} -> {encoded_match}') # progress check

            result = translator.translate(text_to_translate, src=src, dest=dest)
            translated_text = result.text

            # Base16デコードすべき部分を探し、存在する場合はデコードする
            matches = re.findall(r'\{.*?\}', translated_text)
            if matches:
                for match in matches:
                    decoded_match = base16_decode(match[1:-1])
                    translated_text = translated_text.replace(match, '{' + decoded_match + '}')
                    print(f'{match} -> {decoded_match}') # progress check

            matches = re.findall(r'\[.*?\]', translated_text)
            if matches:
                for match in matches:
                    decoded_match = base16_decode(match[1:-1])
                    translated_text = translated_text.replace(match, '[' + decoded_match + ']')
                    print(f'{match} -> {decoded_match}') # progress check

            parts[4] = f'{match_str.group(1)}"{translated_text}"'
            print(f'{match_str.group(1)}"{translated_text}"') # progress check

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
        if filename.startswith('output_') and filename.endswith('.tsv'):
            translate_lines(directory, filename)