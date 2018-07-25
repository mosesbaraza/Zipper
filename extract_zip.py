import zipfile

#method to extract a file from a zip file


def extract_file(zipfilename, filename):
    with zipfile.ZipFile(zipfilename, 'r') as zf:
        zf.extract(filename)
    zf.close()


