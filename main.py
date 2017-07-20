'''
@author: jushitaa

'''
from snrCalc import snrCalc

snrcalc = snrCalc()

'''
snrcalc.rowSplit("rosetta.txt", 100000, 100)
'''
snrcalc.matchTwoFiles("combined_files.txt", "rosetta_100000_1.txt")
