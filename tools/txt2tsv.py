import re
import os

# AwSW-Translator-Toolkitでuntranslated.txtとして出力されたファイルを、ファイル名ごとに分割して*.tsvファイルに変換して保存するプログラム

def sort_data_by_filename(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    txt_files = [f for f in os.listdir(input_directory) if f.endswith('.txt')]

    for input_file in txt_files:
        with open(os.path.join(input_directory, input_file), 'r', encoding='utf-8') as tsvfile:
            data = [line.strip().split('\t') for line in tsvfile]

        sorted_data = sorted(data, key=lambda row: row[0])

        current_filename = None
        current_file = None
        for row in sorted_data:
            filename = row[0]
            # 翻訳上必要ない余計なファイルなのでスキップ
            if re.search(r'game_mods_AwSW-Translator-Toolkit-main_four_tltk_testscene\.rpy.*', filename):
                continue
            match = re.search(r'.*/(.+)\.rpy(?:_\d+)?', filename)
            if match:
                filename = match.group(1)
            if filename != current_filename:
                if current_file is not None:
                    current_file.close()
                current_filename = filename
                safe_filename = current_filename.replace('/', '_').replace(':', '_')
                current_file = open(os.path.join(output_directory, f'{safe_filename}.tsv'), 'w', encoding='utf-8', newline='')
            current_file.write('\t'.join(row) + '\n')
        if current_file is not None:
            current_file.close()

if __name__ == '__main__':
    # ディレクトリの指定
    input_directory = ''
    output_directory = ''

    sort_data_by_filename(input_directory, output_directory)