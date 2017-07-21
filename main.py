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
snrcalc.sortingFiles("rosetta.txt", "combined_files.txt")
