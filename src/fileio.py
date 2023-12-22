from csv import reader
from json import load

def get_paths(path):
    with open(path, "r") as i:
        return reader(i)
    
def get_condval(path):
    with open(path) as cv:
        return load(cv)