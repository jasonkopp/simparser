import re, os, csv, sys
import matplotlib.pyplot as plt
import numpy as np

def getData(directory, codectype):
    resultsCombined = []
    for folder in os.listdir(directory):
        if os.path.isdir(directory+folder):
            for file in os.listdir(directory+folder):
                if file == 'console1':
                    with open(directory+folder+"/"+file, 'r') as console:
                        data = console.read()
                        values = []

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

                    QPval = folder
                    try:
                        QPval = int(QPval[-2:])
                    except ValueError:
                        QPval = int(QPval[-1:])

                    resultsCombined.append([QPval, values])

    resultsCombined = sorted(resultsCombined)
    return (resultsCombined, folder)

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
        csvWriter.writerow(['QP Value', 'Overall1', 'Y1', 'U1', 'V1', 'Bits', 'Avg Overall', 'Avg Y', 'Avg U', 'Avg V', 'Avg Bits'])
        for i in average_data:
            csvWriter.writerow([i[0], i[1][0][0], i[1][0][1], i[1][0][2], i[1][0][3], i[1][0][4], i[1][1][0], i[1][1][1], i[1][1][2], i[1][1][3], i[1][1][4]])


def plot_QPs_Bits(AV1, HEVC, title):
    av1_qps = []
    av1_bits = []
    hevc_qps = []
    hevc_bits = []
    for data in AV1:
        av1_qps.append(int(data[0]))
        av1_bits.append(data[1][1][4])
    for data in HEVC:
        hevc_qps.append(int(data[0]))
        hevc_bits.append(data[1][1][4])

    plt.plot(av1_bits, av1_qps, label='AV1')
    plt.plot(hevc_bits, hevc_qps, label='HEVC')

    plt.xlabel('Bits')
    plt.ylabel('QPs')

    plt.title(title[:-2])
    plt.grid(True)
    plt.legend()
    plt.savefig(title[:-2]+'.png')




warning = 'You need to type "python simparser.py [path/to/AV1/directory] [path/to/HEVC/directory]"'

if len(sys.argv) < 3:
    print("You didn't provide enough arguments.")
    print(warning)

elif len(sys.argv) == 3:
    scriptname = sys.argv[0]
    AV1directory = sys.argv[1] + "/"
    HEVCdirectory = sys.argv[2] + "/"
    print("Running %s..." % scriptname)

    dataAV1 = getData(AV1directory, "av1")
    dataHEVC = getData(HEVCdirectory, "hevc")

    average_dataAV1 = avgData(dataAV1[0], "av1")
    average_dataHEVC = avgData(dataHEVC[0], "hevc")
    title = dataAV1[1]

    makeCSV(average_dataAV1, title+"_av1-data.csv")
    makeCSV(average_dataHEVC, title+"_hevc-data.csv")

    plot_QPs_Bits(average_dataAV1, average_dataHEVC, title)
    plot_QPs_Bits(average_dataAV1, average_dataHEVC, title)

elif len(sys.argv) > 3:
    print("You provided too many arguments.")
    print(warning)
