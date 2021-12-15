#! /usr/bin/python3

import os
import re
import rpm
import subprocess
import sys
import time

# bidirectional class
class bidirectional_iterator:
    def __init__(self, my_list):
#        self.data = ["MyData", "is", "here", "done"]
        self.data = my_list
        self.index = -1

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

# sort function
_nsre = re.compile('([0-9]+)')
def natural_sort_key(s):
   return [int(text) if text.isdigit()
      else text.lower()
      for text in re.split(_nsre, s)
   ]

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

# sort files
file_list.sort(key = natural_sort_key)

it.close()      

###

repeater = bidirectional_iterator(file_list)
itr=iter(repeater)

# First list item
item = next(itr)
os.system('clear')
print()
subprocess.run(["crm_simulate", "-x", item])
print(" #######################################################################")
print()
print ("   Pacemaker transition file:   " + item)
print()
print(" #######################################################################")

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
          os.system('clear')
          print()
          subprocess.run(["crm_simulate", "-x", item])
          print(" #######################################################################")
          print()
          print ("   Pacemaker transition file:   " + item)
          print()
          print(" #######################################################################")
      elif user_input == "p" :
#          print ("p pressed")
          item = reversed(itr)
          os.system('clear')
          print()
          subprocess.run(["crm_simulate", "-x", item])
          print(" #######################################################################")
          print()
          print ("   Pacemaker transition file:   " + item)
          print()
          print(" #######################################################################")
      elif user_input == "c" :
          os.system('clear')
          print()
          print(" #######################################################################")
          print()
          print ("   c pressed - Cu later :-)")
          print()
          print(" #######################################################################")
          print()
          break
   except StopIteration:
      break
