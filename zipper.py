import zipfile
import os


def file_zipper(name, *file_arg):
    file_name=name+".zip"
    with zipfile.ZipFile(file_name, 'w') as zf:
        for data in file_arg:
            for file_obj in os.scandir('.'):
                if data in file_obj.name:
                    zf.write(file_obj.path)
    zf.close()

try:
    file_zipper('file', 'extract_zip')
except zipfile.BadZipFile as zip_err:
    print('Bad File: '+zip_err)
