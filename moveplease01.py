#!/usr/bin/env python3

"""Sarina Lyons | sarina.lyons@tlgcohort.com
   Moving Files Practice"""


# bring in the necessary imports
import shutil
import os

# have Python start the program in the home user directory
os.chdir('/home/student/mycode/')

# move file/folder to desired destination
shutil.move('raynor.obj', 'ceph_storage/')

# prompt user for renaming
xname = input('What is the new name for kerrigan.obj? ')
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)


