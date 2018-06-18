import tarfile
import os
 
def extractAllFilesFromTar(tarfilename):
    with tarfile.TarFile(tarfilename, 'r') as tarStream:
            tarStream.extractall(".")
    tarStream.close()

def extractFileFromTar(tarfilename, filename):
    with tarfile.TarFile(tarfilename, 'r') as tarStream:
            tarStream.extract(filename, ".")
    tarStream.close()

try:
    extractFileFromTar('Desktop.tar', 'main.py')
except KeyError as e:
    print("File inexists: ",e)
