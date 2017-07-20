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
        #newFile = open("expCorr.txt", "w")
        new_input=list()

        with open(_file1, "r") as file:
            file1 = file.readlines()

        with open(_file2, "r") as file:
            file2 = file.readlines();

        for line in file1:
            if line==100:
                break
            striped_line = line.rstrip("\n")
            protein1 = striped_line.split('\t')[0]
            protein2 = striped_line.split('\t')[1]

            for line2 in file2:
                striped_line2 = line2.rstrip("\n")
                protein3 = striped_line2.split('\t')[0]
                protein4 = striped_line2.split('\t')[1]

                if(((protein1 == protein3) and (protein2 == protein4))
                    or ((protein2 == protein3) and (protein1 == protein4))):
                    input_data = "\t".join([protein1, protein2, striped_line2.split('\t')[2]])
                    new_input.append(input_data)

        return (new_input)

    def appendListToFile(self, _file, _list):
        with open(_file,"a+") as file:
            for line in _list:
                file.write(line + "\n")

        print("Done")
