import os

# tsvファイルをRen'Pyのスクリプトファイルに変換するプログラム
# こちらは自動翻訳したものを変換したい人向け
# 内容はstartswith('translated_output_')くらいしか変わっていない

def convert_to_rpy(directory, filename):
    with open(os.path.join(directory, filename), 'r', encoding='utf-8') as infile:
        output_filename = filename.replace('translated_output_', '').replace('.tsv', '.rpy')
        output_path = os.path.join(directory, 'AwSWMod-Japanese', 'resourse', 'tl', 'japanesetl', output_filename)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as outfile:
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
        if filename.startswith('translated_output_') and filename.endswith('.tsv'):
            convert_to_rpy(directory, filename)