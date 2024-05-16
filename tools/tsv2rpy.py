import os

# tsvファイルをRen'Pyのスクリプトファイルに変換するプログラム
# こちらは自動翻訳せずに、output_*.tsvを手動翻訳した人向け
# 内容はstartswith('output_')くらいしか変わっていない

def convert_to_rpy(directory, filename):
    with open(os.path.join(directory, filename), 'r', encoding='utf-8') as infile:
        output_filename = filename.replace('output_', '').replace('.tsv', '.rpy')
        with open(os.path.join(directory, output_filename), 'w', encoding='utf-8') as outfile:
            for line in infile:
                parts = line.split('\t')
                if len(parts) >= 5:
                    label = parts[2].strip()
                    text = parts[4].strip()
                    outfile.write(f'translate japanesetl {label}:\n\n    {text}\n\n')

if __name__ == '__main__':
    # ディレクトリの指定
    directory = ''

    for filename in os.listdir(directory):
        if filename.startswith('output_') and filename.endswith('.tsv'):
            convert_to_rpy(directory, filename)