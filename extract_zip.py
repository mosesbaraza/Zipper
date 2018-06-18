import zipfile


def extract_file(zipfilename, filename):
    with zipfile.ZipFile(zipfilename, 'r') as zf:
        zf.extract(filename)
    zf.close()


