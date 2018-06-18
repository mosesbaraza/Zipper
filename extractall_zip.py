import zipfile

def extractallfiles(zipfilename, dest_path):
    with zipfile.ZipFile(zipfilename, 'r') as zf:
        zf.extractall(dest_path)
    zf.close()

extractallfiles('C:/Users/moses/Downloads/Compressed/python-smsapi-master.zip', 'C:/Users/moses/Downloads/Compressed')

