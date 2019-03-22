# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:27:29 2019

@author: Donghyun Kang
"""

import os 
import pandas as pd
import matplotlib.pyplot as plt

#Extracting people if one's major field of study contains "neuro"
neuro_only = open("neuro_people.tsv", encoding = "utf-8", mode = "w")

with open(".\\original_data\\people_utf8.tsv", "r", encoding = "utf-8") as f:
    for line in f.readlines():
        split = line.split("\t")
        if split[0] == "\"pid\"":
            neuro_only.write(line)
        if "neuro" in split[8]:
            neuro_only.write(line)
                
neuro_only.close()

#making set for pid
pid_set = set([])
with open("neuro_people.tsv", "r", encoding = "utf-8", ) as f:
    for line in f.readlines():
        pid = line.split("\t")[0].strip("\"")
        pid_set.update([pid])


#Extracting the relationship data using pid
neuro_rel = open("neuro_relation.tsv", encoding = "utf-8", mode = "w")

con_file = open(".\\original_data\\connection_utf8.tsv", "r", encoding = "utf-8")
 
header = con_file.readline()
neuro_rel.write(header)

lines = con_file.readlines()
for line in lines[1:]:    
    split = line.split("\t")
    pid_1 = split[1].strip("\"")
    pid_2 = split[2].strip("\"")
    if pid_1 in pid_set or pid_2 in pid_set:
        neuro_rel.write(line)
                
neuro_rel.close()
con_file.close()