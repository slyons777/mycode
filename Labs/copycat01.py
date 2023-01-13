#!/usr/bin/env python3

"""Sarina Lyons | sarina.lyons@tlgcohort.com
   Copying files and folders"""

# import additional code
import shutil
import os

# move into working directory
os.chdir("/home/student/mycode/")

# creates file copies
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

# copies full directory
shutil.copytree("5g_research/", "5g_research_backup/")


