import os

import sort
import translate_tsv
import tsv2rpy_trans
import txt2tsv

def main():
    # AwSW-Translator-Toolkitでuntranslated.txtとして出力されたファイルを入れたパスをここに入力してください。
    directory = ''

    txt2tsv.sort_data_by_filename(directory, directory)

    files = os.listdir(directory)

    for filename in files:
        if filename.endswith('.tsv'):
            sorted_filename = sort.sort_lines(directory, filename)
            translated_filename = translate_tsv.translate_lines(directory, sorted_filename)
            tsv2rpy_trans.convert_to_rpy(directory, translated_filename)

if __name__ == "__main__":
    main()