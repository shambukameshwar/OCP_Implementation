import shutil
import zipfile
import os

def zrchive_directory(output_filename,dir_name):
    shutil.make_archive(output_filename, 'zip', dir_name)
    zrchive_directory_initial_zipFileDelete(output_filename)
    fileToRemove=output_filename+'.zip'
    os.remove(fileToRemove)
    return('Archiving Successful')

def zrchive_directory_initial_zipFileDelete(output_filename):
    inputZipFile=output_filename+'.zip'
    outputZipFile=output_filename+'[pack]'+'.zip'
    zin = zipfile.ZipFile (inputZipFile, 'r')
    zout = zipfile.ZipFile (outputZipFile, 'w')
    for item in zin.infolist():
        buffer = zin.read(item.filename)
        if (item.filename[-4:] != '.zip'):
            zout.writestr(item, buffer)
    zout.close()
    zin.close()
