'''
@author: jushitaa

'''
from snrCalc import snrCalc

snrcalc = snrCalc()

'''
snrcalc.rowSplit("rosetta.txt", 1000000, 100)
'''

snrCalc.appendListToFile("expCor.txt", snrCalc.matchTwoFiles("combined_files.txt", "test.txt","test.txt"))
'''
snrCalc.matchTwoFiles("combined_files.txt","test.txt","test.txt")
'''
