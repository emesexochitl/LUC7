# Fishers exact test

######################################################

exonnum = ">=10"
circ1 = nrow(diff_table2[ which(diff_table2$`No. of exons` == exonnum & diff_table2$Type == "circ"), ])
circtotal = 1609
circ2= circtotal - circ1

lin1= nrow(diff_table2[ which(diff_table2$`No. of exons` == exonnum & diff_table2$Type == "lin"), ])
lintotal= 54013
lin2= lintotal - lin1

ct <- matrix(c(circ1, circ2, lin1, lin2), nrow = 2, ncol = 2)
#last

#middle

colnames(ct) <- c("y", "n")
rownames(ct) <- c("inv", "rest")
ct
fisher.test(ct, alternative = "two.sided")
fisher.test(ct, alternative = "greater")
fisher.test(ct, alternative = "less")
#first

