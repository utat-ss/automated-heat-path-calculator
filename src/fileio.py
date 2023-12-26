from csv import reader
from json import load

"""
        Return a list containing the csv file contents
"""
def get_paths(path):
        with open(path, "r") as i:
                return list(reader(i))

"""
        Return a dictionary containing the json file contents
"""
def get_condval(path):
        with open(path) as cv:
                return load(cv)
    
def file_output(path, content, mode):
        with open(path, mode) as ofile:
             ofile.write(content)