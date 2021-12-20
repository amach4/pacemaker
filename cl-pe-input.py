#! /usr/bin/python3

# Name: cl-pe-input.py
# Author: Andreas Mach
# Date: 16-12-2021
# Created with Python 3.6.12

"""This script was created to search for Pacemaker transition files in the current directory.
The script is searching for files starting with "pe-input" and end with ".bz2".
The files will be sorted on natural basis and a Python list will be created.
The elements of the list wil be used to execute "crm_simulate -x <element>" and the status
of the Pacemaker cluster will be shown in a formatted output in the console."""


import os
import re
import rpm
import subprocess
import sys
import time


class bidirectional_iterator:
    """
    step forward and backward depending on the current list element
    """
#    def __init__(self):
    def __init__(self, my_list, start_item):
#        self.data = ["erste", "1", "MyData", "is", "here", "done"]
        self.data = my_list
        self.index = start_item_index

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index >= len(self.data):
            raise StopIteration
        return self.data[self.index]

    def __reversed__(self):
        self.index -= 1
        if self.index == -1:
            raise StopIteration
        return self.data[self.index]
###

_nsre = re.compile('([0-9]+)')
def natural_sort_key(s):
   """
   natural sort
   """
   return [int(text) if text.isdigit()
      else text.lower()
      for text in re.split(_nsre, s)
   ]

###

def proc():
   """
   execute subprocess and format output
   """
   proc = subprocess.Popen(["crm_simulate", "-x", item], stdout=subprocess.PIPE, universal_newlines=True)
   for line in proc.stdout:
      print("   ", line.strip())

###

def name():
   """
   Item name output
   """
   print (" #######################################################################")
   print ()
   print ('\33[32m' + "   Pacemaker transition file:   " + item + '\33[0m' )
   print ()
   print (" #######################################################################")

###   

# open rpm database and verify if "pacemaker-cli" package is installed
print()
ts = rpm.TransactionSet()
mi = ts.dbMatch( 'name', 'pacemaker-cli' )
try :
    h = mi.__next__()
    print ("%s-%s-%s.%s" % (h['name'].decode(), h['version'].decode(), h['release'].decode(), h['arch'].decode()))
except StopIteration:
    print ("Package not found")
print()

###

# search for files only in the current directory which start with "pe-input" and end with ".bz2" and sort them by digits in the file name
path = '.'
it = os.scandir(path)

# search for files
file_list = [ entry.name for entry in it if entry.name.startswith("pe-input") and entry.name.endswith(".bz2") and entry.is_file()]

# verify if list is empty
if len(file_list) == 0:
    print ()
    print("No such files, your list is empty!!!")#
    print ()
    exit()

# sort files
file_list.sort(key = natural_sort_key)

it.close()      

###

# Ask for initial list item
os.system('clear')
print ()
print ('   Please enter initial Pacemaker transition file name ( Example: "pe-input-20.bz2" ).')
print ()
start_item = input('   Filename:   ')
print ()

start_item_index = file_list.index(start_item)
repeater = bidirectional_iterator(file_list, start_item)
itr=iter(repeater)
item = start_item

os.system('clear')
print ()
proc() # function: proc
name() # function: name 

#print ("next: ", next(itr))
#print ("prev: ", reversed(itr))

while True:

   print()
   user_input = input("   Press: p (previous) or n (next) or c (cancel) :    ")
   print()

   try:
      if user_input == "n" :
#          print ("n pressed")
          item = next(itr)
#          item = next(itr)
#           item = "pe-input-301.bz2"
          os.system('clear')
          print ()
          proc() # function: proc
          name() # function: name 
      elif user_input == "p" :
#          print ("p pressed")
          item = reversed(itr)
          os.system('clear')
          print ()
          proc() # function: proc
          name() # function: name 
      elif user_input == "c" :
          os.system('clear')
          print ()
          print (" #######################################################################")
          print ()
          print ("   c pressed - Cu later \33[32m :-) \33[0m")
          print ()
          print (" #######################################################################")
          print ()
          break
   except StopIteration:
      break
