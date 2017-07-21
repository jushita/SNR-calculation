'''
@author: jushitaa

'''
from snrCalc import snrCalc

snrcalc = snrCalc()

'''
snrcalc.rowSplit("rosetta.txt", 100000, 1)


snrcalc.appendListToFile("expCor.txt", snrCalc.matchTwoFiles("combined_files.txt", "test.txt","test.txt"))

snrcalc.matchTwoFiles("combined_files.txt","test.txt","test.txt")
'''
for i in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]:
    snrcalc.sortingFiles("rosetta.txt", "combined_files_" + str(i) + ".txt", 0.7)
