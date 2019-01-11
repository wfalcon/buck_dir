#!/usr/bin/env python3
import datetime
import shutil
import sys
import os

info = "use: back_dir.py /dir_backup /target_dir_for_gztar 'type'"


def backup_dir(s, d, f='gztar'):
    """
    Функция делает рекурсивно gztar архив содержимого каталога
    :param s: в каталог :param d: с именем :param s + current_datetime.
    Если каталог :param d отсутствует, то он будет создан.
    Необязательный :param f определяет тип архива(по умолчанию 'gztar'):
    'bztar', "bzip2'ed tar-file,
    'gztar', "gzip'ed tar-file,
    'tar',   'uncompressed tar file',
    'xztar', "xz'ed tar-file",
    'zip',   'ZIP file'
    Например: backup_dir('/root','/home', 'zip')
    """
    if s and d and f:
        if os.path.isdir(s) and len(os.listdir(s)) > 0:
            shutil.make_archive(d + '/' + str(datetime.datetime.now()), f, s)
            return True
        else:
            print('Empty')
    else:
        print(info)


if __name__ == "__main__":
    if len(sys.argv) == 3 or len(sys.argv) == 4:
        path_sourse = sys.argv[1]
        path_destination = sys.argv[2]
        if len(sys.argv) == 3:
            type = 'gztar'
        else:
            type = sys.argv[3]
        backup_dir(path_sourse, path_destination, type)
        print('ok')
    else:
        print(info)
