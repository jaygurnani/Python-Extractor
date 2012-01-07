#!/usr/bin/python
#Author: Jay Gurnani
#Description: A Python based extrator for compressed formats

from sys import argv, exit #Importing required sys modules
import os #Importing os module
import zipfile #Importing zip module
import tarfile #Importing tar module

#Global Variables
path_to_extract = "unzip"

#Extracting zip file
def zip_extract(to_extract):
    zp = zipfile.ZipFile(to_extract, 'r')
    print "%s is a Zip File" % (to_extract)
    if not os.path.exists(path_to_extract):
       os.makedirs(path_to_extract)
    else: 
       answer = raw_input('Directory Exists, if files exists, they will be overwritten. y/n?')
       if (answer == "n"):
           exit(0)
    if (zp.testzip() != None):
        print "Corrupted File at %s" % zp.testzip()
        exit(0)
    for file in zp.namelist():
        zp.extract(file, path_to_extract)
	print 'Extracting %s to /%s' % (file, path_to_extract) 
    zp.close()

#Extracting tar file
def tar_extract(to_extract):
    (name, file_ext) = os.path.splitext(to_extract)
    if (file_ext == ".gz"):
        print "%s is a .gz File" % (to_extract)
    elif (file_ext == ".bz2"):
        print "%s is a .bz2 File" % (to_extract)
    else: 
        print "%s is a .tar File" % (to_extract) 
    tr = tarfile.open(to_extract, 'r')
    tarinfo = tarfile.TarInfo(tr)
    if not os.path.exists(path_to_extract):
        os.makedirs(path_to_extract)
    else:
       answer = raw_input('Directory Exists, if files exists, they will be overwritten. y/n?')
       if (answer == "n"):
           exit(0)
    if (tarinfo.isfile() != True):
        print "Corrupted File"
        exit(0)
    for file in tr.getnames():
        tr.extract(file, path_to_extract)
        print 'Extracting %s to /%s' % (file, path_to_extract)
    tr.close()

#Checker function
def checker (argument):
    if (zipfile.is_zipfile(argument)):
        zip_extract(argument)
    elif (tarfile.is_tarfile(argument)): 
        tar_extract(argument)
    else:
        print "Cannot recognize format. Only .zip, .tar, .gz and .bz2 supported"
        exit(0)

#Main Function
def main (argm):
    if len(argm) < 1:
        print "Wrong Syntax. Required format = ./extrator.py argument.zip"
        exit(0)
    else:
        checker(argm)

