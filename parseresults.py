#!/bin/env/python

from os import listdir
from os.path import isfile, join
onlyfiles = [ f for f in listdir(mypath) if isfile(join("imas_a_*",f)) ]

# Read mode opens a file for reading only.
try:
  f = open("file.txt", "r")
  try:
    # Read the entire contents of a file at once.
    string = f.read()
    # OR read one line at a time.
    line = f.readline()
    # OR read all the lines into a list.
    lines = f.readlines()
  finally:
    f.close()
except IOError:
  pass
