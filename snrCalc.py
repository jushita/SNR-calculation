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

    ##NEW APPROACH

    def sortingFiles(self, _file, _file2):
        dict_rosetta = dict()
        signal = 0
        noise = 0
        with open(_file, "r") as file:
            for line in file:
                striped_line = line.rstrip("\n")
                pp = striped_line.split('\t')[0:3] #two proteins are in pp list
                pp = sorted(pp)
                #print(pp)
                #joining two proteins to make key
                _key = "\t".join(pp[1:3])
                _value = pp[0]

                #_value = pp[0]
                #print (_key, _value)
                dict_rosetta[_key] = _value
            #print (dict_rosetta)

        #sorting AB BA problem
        listOfFiles = list()
        with open(_file2, "r") as file:
            for i, line2 in enumerate(file):
                striped_line2= line2.rstrip("\n")
                split_line2 = striped_line2.split("\t")
                split_line2 = sorted (split_line2)
                listOfFiles.append("\t".join(split_line2[1:3]))

        for i, pp in enumerate(listOfFiles):
            if pp in dict_rosetta:
                if (float(dict_rosetta[pp])) >= 0.7:
                    signal += 1
                else:
                    noise += 1
        print (signal, noise)
