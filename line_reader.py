import os

def file_reader(filename):
    if not os.path.exists(filename):
        raise Exception("Bad Filename")
    infile = open(filename, "r")
    line = infile.readline()
    return line
