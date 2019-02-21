#!/usr/bin/python

import datetime

input="Arabidopsis_thaliana_ensembl33_allisoform_exonnum.txt"

inputs=[]
with open(input) as inputfile:
    for line in inputfile:
       inputs.append(line.strip().split(' '))

input1=[item[0] for item in inputs]
input2=[item[1] for item in inputs]
input3=[item[2] for item in inputs]
input4=[item[3] for item in inputs]
input5=[item[4] for item in inputs]
input6=[item[5] for item in inputs]
input7=[item[6] for item in inputs]
input8=[item[7] for item in inputs]
input9=[item[8] for item in inputs]

numfile="Arabidopsis_thaliana_ensembl33_allisoform_exonnums_eqm3.csv"

nums=[]
with open(numfile) as inputfile:
    for line in inputfile:
       nums.append(line.strip().split(','))

num1=[item[0] for item in nums]
num2=[item[1] for item in nums]

outfile="Arabidopsis_thaliana_ensembl33_isoform_eqm3.txt"

myfile= open(outfile, "w")


for i in xrange(0,len(inputs)):
    for j in xrange(0,len(nums)):   
        hit=False

        if input3[i]==num1[j]:
            #print input1[i], input2[i], input3[i], input4[i], input5[i], input6[i], input7[i], input8[i], num2[j] 
            myfile.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (input1[i], input2[i], input3[i], input4[i], input5[i], input6[i], input7[i], input8[i], input9[i], num2[j]))
            hit=True
            break
        elif input3[i]!=num1[j]:
            continue
        
    #if hit == False:
        #print ref1[i], ref2[i], ref3[i], ref4[i], ref5[i], ref6[i], "n/a", "n/a", "n/a", "no"


myfile.close()
