import re, os, csv, sys

def getData(directory, codectype):
    resultsCombined = []
    for folder in os.listdir(directory):
        if os.path.isdir(directory+folder):
            for file in os.listdir(directory+folder):
                if file == 'console1':
                    with open(directory+folder+"/"+file, 'r') as console:
                        data = console.read()
                        values=[]

                        if codectype == "av1":
                            pattern = r'([\d]+.[\d]{3}) ([\d]+.[\d]{3}) ([\d]+.[\d]{3}) ([\d]+.[\d]{3})[\s]+([\d]+)F'
                            for m in re.finditer(pattern, data):
                                overval = float(m.group(1))
                                yval    = float(m.group(2))
                                uval    = float(m.group(3))
                                vval    = float(m.group(4))
                                bits    = float(m.group(5))*8
                                values.append([overval, yval, uval, vval, bits])

                        elif codectype == "hevc":
                            pattern = r'([\d]+) bits \[Y ([\d]+.[\d]+) dB    U ([\d]+.[\d]+) dB    V ([\d]+.[\d]+)'
                            for m in re.finditer(pattern, data):
                                overval = '-'
                                bits    = float(m.group(1))
                                yval    = float(m.group(2))
                                uval    = float(m.group(3))
                                vval    = float(m.group(4))
                                values.append([overval, yval, uval, vval, bits])

                    resultsCombined.append([folder, values])
    resultsCombined = sorted(resultsCombined)
    return resultsCombined

def avgData(newdata, codectype):
    listOverall = []
    listY       = []
    listU       = []
    listV       = []
    listbits    = []

    for i in range(len(newdata)):
        firstOverall    = newdata[i][1][0][0]
        firstY          = newdata[i][1][0][1]
        firstU          = newdata[i][1][0][2]
        firstV          = newdata[i][1][0][3]
        firstBits       = newdata[i][1][0][4]

        for j in range(len(newdata[i][1])):
            listOverall.append(newdata[i][1][j][0])
            listY.append(newdata[i][1][j][1])
            listU.append(newdata[i][1][j][2])
            listV.append(newdata[i][1][j][3])
            listbits.append(newdata[i][1][j][4])

        if codectype == "av1":
            newdata[i][1] = [[firstOverall, firstY, firstU, firstV, firstBits], [findaverage(listOverall), findaverage(listY), findaverage(listU), findaverage(listV), findaverage(listbits)]]

        elif codectype == "hevc":
            newdata[i][1] = [[firstOverall, firstY, firstU, firstV, firstBits], ['-', findaverage(listY), findaverage(listU), findaverage(listV), findaverage(listbits)]]
    return newdata

def findaverage(list):
    return round((sum(list) / len(list)),3)

def makeCSV(average_data, newfilename):
    with open(newfilename, 'w') as newFile:
        csvWriter = csv.writer(newFile)
        csvWriter.writerow(['Folder Name', 'Overall1', 'Y1', 'U1', 'V1', 'Bits', 'Avg Overall', 'Avg Y', 'Avg U', 'Avg V', 'Avg Bits'])
        for i in average_data:
            csvWriter.writerow([i[0], i[1][0][0], i[1][0][1], i[1][0][2], i[1][0][3], i[1][0][4], i[1][1][0], i[1][1][1], i[1][1][2], i[1][1][3], i[1][1][4]])

warning = 'You need to type "python simparser.py [path/to/directory] [codec type] [*optional* newfilename]"'

if len(sys.argv) <= 2:
    print("You didn't provide enough arguments.")
    print(warning)

elif len(sys.argv) == 3:
    scriptname = sys.argv[0]
    directory = sys.argv[1] + "/"
    codectype = sys.argv[2].lower()
    newfilename = codectype + "-test.csv"
    print("Running %s on %s (codectype=%s) > %s" % (scriptname, directory, codectype, newfilename))

    data = getData(directory, codectype)
    average_data = avgData(data, codectype)
    makeCSV(average_data, newfilename)

elif len(sys.argv) == 4:
    scriptname = sys.argv[0]
    directory = sys.argv[1] + "/"
    codectype = sys.argv[2].lower()
    newfilename = sys.argv[3]
    print("Running %s on %s (codectype=%s) > %s" % (scriptname, directory, codectype, newfilename))

    data = getData(directory, codectype)
    average_data = avgData(data, codectype)
    makeCSV(average_data, newfilename)

elif len(sys.argv) > 4:
    print("You provided too many arguments.")
    print(warning)
