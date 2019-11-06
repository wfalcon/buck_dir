# buck_dir
The function makes recursively gztar archive directory contents</br>
 Функция делает рекурсивно gztar архив содержимого каталога</br>
    :param s: в каталог :param d: с именем :param s + current_datetime.</br>
    Если каталог :param d отсутствует, то он будет создан.</br>
    Необязательный :param f определяет тип архива(по умолчанию 'gztar'):</br>
    'bztar', "bzip2'ed tar-file,</br>
    'gztar', "gzip'ed tar-file,</br>
    'tar',   'uncompressed tar file',</br>
    'xztar', "xz'ed tar-file",</br>
    'zip',   'ZIP file'</br>

