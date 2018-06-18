import tarfile
import os

def write_a_tarfile(tarfilename, *files):
    with tarfile.open(tarfilename, 'w|') as tarStream:
        for data in files:
            for file_obj in os.scandir("."):
                if data in file_obj.name:
                    tarStream.add(file_obj.path)
    tarStream.close()

