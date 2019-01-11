# buck_dir
The function makes recursively gztar archive directory contents</br>
 Функция делает рекурсивно gztar архив содержимого каталога
    :param s: в каталог :param d: с именем :param s + current_datetime.
    Если каталог :param d отсутствует, то он будет создан.
    Необязательный :param f определяет тип архива(по умолчанию 'gztar'):
    'bztar', "bzip2'ed tar-file,
    'gztar', "gzip'ed tar-file,
    'tar',   'uncompressed tar file',
    'xztar', "xz'ed tar-file",
    'zip',   'ZIP file'
