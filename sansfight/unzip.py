import zipfile
import os

def unzip():
    filename = "res.zip"
    '''解压资源文件'''
    if not os.path.exists(os.path.splitext(filename)[0]):
        os.mkdir(os.path.splitext(filename)[0])
        zip_file = zipfile.ZipFile(filename)
        if os.path.isdir(os.path.splitext(filename)[0]):
            zip_list = zip_file.namelist()
        for f in zip_list:
            zip_file.extract(f, os.path.splitext(filename)[0])
        zip_file.close()
