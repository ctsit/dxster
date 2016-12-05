# -*- coding: utf-8 -*-

import sys
import os
sys.path.insert(0, os.path.abspath('../..'))

import dxster
import csv

#print dxster.calc_dxster(4.5,'lmci')

in_file= open('sample_data.csv', "rb")
f_reader= csv.reader(in_file)

rownum=0
for row in f_reader:
    #grab the header to write out later
    if rownum==0:
        header = rownum
    else:

        a_npdx = str(row[1])
        b_cdrsb = float(row[2])
        c_algdx = dxster.calc_dxster(b_cdrsb,a_npdx)
        print "a_npdx=" + a_npdx, b_cdrsb, c_algdx


        #print dxster.calc_dxster(b_cdrsb,a_npdx)

        #print 'subject_id:' + row[0], 'NPDx:' + row[1], 'CDR_SB:' + row[2]

    rownum+=1
in_file.close()
