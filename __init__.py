from modloader.modclass import Mod, loadable_mod

import os
import re
import codecs
import json
# import shutil

@loadable_mod
class AWSWMod(Mod):
    def mod_info(self):
        return ("AwSWMod-Japanese", "v0.4.2", "DragoSuzuki58")

    def mod_load(self):
            # 以下は、Pythonスクリプトを読み込んで、特定の場所を日本語訳するスクリプトです
            # 他のModのコードに干渉するので注意
            with codecs.open('game/mods/AwSWMod-Japanese/assets/translations.json', 'r', encoding='utf-8') as f:
                translations = json.load(f)

                for directory, files in translations.items():
                    try:
                        for file_name, translation_map in files.items():
                            original_file = os.path.join("game/mods/", directory, file_name)

                            if not os.path.exists(original_file):
                                raise OSError('File not found')

                            with codecs.open(original_file, 'r', encoding='utf-8') as f:
                                content = f.read()

                            if not content[0].startswith('# -*- coding: utf-8 -*-'):
                                content.insert(0, '# -*- coding: utf-8 -*-\n')

                            # バックアップファイルを作成する予定だったが、それをModと認識してしまってエラーが出るため、一旦保留
                            # 詳しい方は、backup_dirから下をコメントアウトして絶対パスに変更すれば、バックアップファイルを作成できると思います。
                            # backup_file = os.path.join("game/mods/AwSWMod-Japanese/backup",directory, file_name + ".bak")
                            # backup_dir = os.path.dirname(backup_file)
                            # if not os.path.exists(backup_dir):
                            #     os.makedirs(backup_dir)
                            # shutil.copyfile(original_file, backup_file)

                            for original, translation in translation_map.items():
                                pattern = re.escape(original)
                                replacement = translation
                                content = re.sub(pattern, replacement, content)

                            with codecs.open(original_file, 'w', encoding='utf-8') as f:
                                f.write(content)

                    except OSError:
                        pass

    def mod_complete(self):
        pass