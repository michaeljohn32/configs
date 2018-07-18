#!/usr/bin/python
CONFIGFILE="myconfigfile.txt"

def read_file(filename):
  with open(filename) as myfile:
    filelines = myfile.readlines()
  filelines = [line.strip() for line in filelines]
  return filelines
def split_lines(values):
  env = {}
  for line in values:
    keypair = line.split('=')
    keypair = [val.strip() for val in keypair]
    env[keypair[0]] = keypair[1]
  return env

lines = read_file(CONFIGFILE)
environment_dict = split_lines(lines)
for key, value in environment_dict.items():
  print('export '+key+'="'+value+'"')

