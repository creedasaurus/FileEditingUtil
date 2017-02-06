# Tanner Frandsen
# Archive Number AV-47013
# Purpose: Add override to the files found in list.txt
#           format for list .txt is [file Name], [Line Number]


import re, os

print "    Starting the program    "
print "--------------------------------"
fileLoc = []  # store the file locations
lineNum = []  # store the line numbers to edit
line = ""
index = -1
LinesChanged = 0;

# read in the list and parse to the appropriate arrays
with open("C:\\Users\\tfrandsen\\Desktop\\TestFolder\\List_Nullptr.txt") as changeList:
    while True:
        line = changeList.readline()
        if not line:
            break
        tempList = re.split(',', line.strip('\n'))
        fileLoc.append(tempList[0].strip())
        lineNum.append(int(tempList[1]))

# open the files
for elem in fileLoc:
    index += 1
    changeLn = lineNum[index]
    lnNum = 1

    if os.path.isfile(elem):
        filedata = []
		
		#Open File and Read Into an Array
        with open(elem, 'r') as filet:
            for line in filet:
                filedata.append(line)

		#Looping Through the ARRAY (Not File) by Index, and Making Changes as needed
        for l_index in range(len(filedata)):
            line = filedata[l_index]
            stripped_line = line.strip()
            if lnNum == changeLn:
                if "{" in stripped_line:
                    filedata[l_index] = line.replace("{", "override {")
                    LinesChanged += 1
                elif stripped_line.endswith(";") or "//" in line:
                    tempstring = line.replace(";", " override;")
                    filedata[l_index] = line.replace(";", " override;")
                    LinesChanged += 1
                elif stripped_line.endswith(")"):  # foo() replace ")" with ") override"
                    filedata[l_index] = line.replace(")", ") override")
                    LinesChanged += 1
                elif stripped_line.endswith("const"): # replace "const" with "const override" this will catch const \n {
                    filedata[l_index] = line.replace("const", "const override")
                    LinesChanged += 1
            lnNum += 1

		#Opening File and Writing the Lines Back Out FROM the array
        with open(elem, 'w') as filet:
            for line in filedata:
                filet.write(line)
    else:
        print "File Doesn't Exist:", elem


print "--------------------------------"
print "    Ending program...    " + "Lines Changed: " + str(LinesChanged)
