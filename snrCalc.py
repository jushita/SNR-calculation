import os

'''
@author: jushitaa

'''
class snrCalc():
    def rowSplit(self, _file, num_row, num_files):
        file_counter = 0;
         #open file
        with open(_file, "r") as file:
            #loop throught each line of file
            for i, line in enumerate(file):

                #check if we're at a 500,000 mark
                if i%num_row == 0:
                    if (file_counter >= num_files) and i != 0:
                        break

                    #create open new file to write to
                    new_file = open(os.path.basename(_file).split(".")[0] + "_" + str(num_row) + "_" + str(file_counter + 1) + ".txt", "w")
                    file_counter += 1

                #write current line to new file
                new_file.write(line)

        print("Done!")
    def matchTwoFiles(self,_file1,_file2):
        newFile = open("expCorr.txt", "w")
        with open(_file1, "r") as file1:
                for i, line in enumerate(file1):
                    if i==100:
                        break

                    line = line.rstrip("\n")
                    protein1=line.split('\t')[0]
                    protein2=line.split('\t')[1]
                    with open(_file2, "r") as file2:
                        for j, line2 in enumerate(file2):

                            line2 = line2.rstrip("\n")
                            protein3 = line2.split('\t')[0]
                            protein4 = line2.split('\t')[1]

                            if (((protein1==protein3) and (protein2==protein4)) or ((protein2==protein3) and (protein1==protein4))):
                                input_data = ("\t".join((protein1, protein2)))
                                newFile.write(input_data + "\n")
        print("Done")
