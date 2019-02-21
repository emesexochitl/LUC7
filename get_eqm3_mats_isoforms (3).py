#!/usr/bin/python

#import datetime

matsfile="mats_ri_rtjc_cold24h_all_events.txt"

mats=[]
with open(matsfile) as inputfile:
    for line in inputfile:
        mats.append(line.strip().split('\t'))

mats1=[item[1] for item in mats]
mats2=[item[4] for item in mats]
mats3=[item[7] for item in mats]
mats4=[item[8] for item in mats]
mats5=[item[9] for item in mats]
mats6=[item[10] for item in mats]

reffile="Arabidopsis_thaliana_ensembl33_isoform_eqm3_man.txt"

refs=[]
with open(reffile) as inputfile:
    for line in inputfile:
        refs.append(line.strip().split('\t'))

ref1=[item[0] for item in refs]
ref2=[item[2] for item in refs]
ref3=[item[5] for item in refs]
ref4=[item[6] for item in refs]
ref5=[item[7] for item in refs]
ref6=[item[8] for item in refs]
ref7=[item[9] for item in refs]

outfile="Arabidopsis_thaliana_ensembl33_isoform_eqm3_ri_mats_rotajc_all_cold24h.txt"
myfile= open(outfile, "w")

left1 = 0
left2 = 0
right1 = 0
right2 = 0
firstnum = 0
midnum = 0
lastnum = 0

for i in xrange(0,len(mats)):
    left1 = 0
    left2 = 0
    right1 = 0
    right2 = 0
    maxexon = 0

    for j in xrange(0,len(refs)):   
        
   
        if mats1[i]==ref1[j] and mats3[i]==ref4[j] and mats4[i]==ref5[j]:
            hit = True
            gene =  mats1[i]
            gene_id1 = ref2[j]
            left1 = mats3[i]
            left2 = mats4[i]
            exon1 = int(ref3[j])
               
                
        if mats1[i]==ref1[j] and mats5[i]==ref4[j] and mats6[i]==ref5[j]:
            hit = True
            gene =  mats1[i]
            gene_id2 = ref2[j]
            right1 = mats5[i]
            right2 = mats6[i]
            exon2 = int(ref3[j])
            maxexon = ref7[j]

    if left1 == 0 or left2 == 0 or right1 == 0 or right2 == 0:
        continue
    if exon1 == exon2:
        continue
    
    if exon2-exon1 > 1 or exon1-exon2 > 1:

        for k in xrange(0,len(refs)):
            
            if gene == ref1[k] and gene_id1 == ref2[k] and int(ref3[k]) == exon1+1 and ref4[k] == right1 and ref5[k] == right2:
                gene_id2 = ref2[k]
                right1 = ref4[k]
                right2 = ref5[k]
                exon2 = ref3[k]
                maxexon = ref7[k]
                break

            if gene == ref1[k] and gene_id2 == ref2[k] and int(ref3[k]) == exon1+1 and ref4[k] == left1 and ref5[k] == left2:
                gene_id1 = ref2[k]
                left1 = ref4[k]
                left2 = ref5[k]
                exon1 = ref3[k]
                maxexon = ref7[k]
                break
 
            if gene == ref1[k] and gene_id1 == ref2[k] and int(ref3[k]) == exon2+1 and ref4[k] == right1 and ref5[k] == right2:
                gene_id2 = ref2[k]
                right1 = ref4[k]
                right2 = ref5[k]
                exon2 = ref3[k]
                maxexon = ref7[k]
                break

            if gene == ref1[k] and gene_id2 == ref2[k] and int(ref3[k]) == exon2+1 and ref4[k] == left1 and ref5[k] == left2:
                gene_id1 = ref2[k]
                left1 = ref4[k]
                left2 = ref5[k]
                exon1 = ref3[k]
                maxexon = ref7[k]
                break      
                 
            if gene == ref1[k] and gene_id1 == ref2[k] and int(ref3[k]) == exon1-1 and ref4[k] == right1 and ref5[k] == right2:
                gene_id2 = ref2[k]
                right1 = ref4[k]
                right2 = ref5[k]
                exon2 = ref3[k]
                maxexon = ref7[k]
                break                       
            else:
                continue
            
        intron = 0
         
        if  int(exon1)==1 and int(exon2)==2:
            intron = "first"
            firstnum = firstnum + 1
        elif  int(exon1)==2 and int(exon2)==1:
            intron = "first"
            firstnum = firstnum + 1            
        elif int(exon2)==int(maxexon) and int(exon1) == int(maxexon)-1:
            intron = "last"
            lastnum = lastnum + 1
        elif int(exon1)==int(maxexon) and int(exon2) == int(maxexon)-1:
            intron = "last"
            lastnum = lastnum + 1
        else:
            intron = "middle"
            midnum = midnum + 1
            
        print gene, gene_id1, gene_id2, left1, left2, right1, right2, exon1, exon2, mats2[i], maxexon, intron, "exep"
        myfile.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\texep\n" % (gene, gene_id1, gene_id2, left1, left2, right1, right2, exon1, exon2, mats2[i], maxexon, intron))
            
    else:
        intron = 0          
        if  exon2==1 and exon1==2:
            intron = "first"
            firstnum = firstnum + 1

        elif  exon2==2 and exon1==1:
            intron = "first"
            firstnum = firstnum + 1
        elif int(exon2)==int(maxexon) and int(exon1) == int(maxexon)-1:
            intron = "last"
            lastnum = lastnum + 1
        elif int(exon1)==int(maxexon) and int(exon2) == int(maxexon)-1:
            intron = "last"
            lastnum = lastnum + 1
        else:
            intron = "middle"
            midnum = midnum + 1

        print gene, gene_id1, gene_id2, left1, left2, right1, right2, exon1, exon2, mats2[i], maxexon, intron, "reg"   
        myfile.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\treg\n" % (gene, gene_id1, gene_id2, left1, left2, right1, right2, exon1, exon2, mats2[i], maxexon, intron))
   
print firstnum, midnum, lastnum

myfile.close()
